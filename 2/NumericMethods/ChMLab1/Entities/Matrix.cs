using System;
using System.Collections.Generic;

namespace ChMLab1
{
    class Matrix
    {
        double[,] m = { };
        
        public Matrix(double[,] m)
        {
            this.m = m;
        }

        public double this[int n, int m] => this.m[n,m];

        public static List<double> operator *(Matrix a, List<double> b)
        {
            var ret = new List<double>();
            for(int i = 0; i < b.Count; i++)
            {
                var r = a.GetRow(i);
                double member = 0;
                for(int j = 0; j < b.Count; j++)
                {
                    member += b[j] * r[j];
                }
                ret.Add(member);
            }
            return ret;
        }

        public List<double> GetRow(int n)
        {
            var r = new List<double>();
            for(int i = 0; i < m.GetLength(0); i++)
                r.Add(m[n,i]);
            return new List<double>(r);
        }

        public void SetRow(int n, List<double> l)
        {
            for (int i = 0; i < m.GetLength(0); i++)
                m[n, i] = l[i];
        }

        public void DiffRows(int n, int m, double c)
        {
            var rn = GetRow(n);
            var rm = GetRow(m);
            for (int i = 0; i < rn.Count; i++)
                rm[i] -= rn[i]/c;
            SetRow(m, rm);
        }

        public void DivRow(int n, double d)
        {
            var b = GetRow(n);
            for (int i = 0; i < b.Count; i++)
                b[i] /= d;
            SetRow(n, b);
        }
        public void ColNormalize(int n, int m)
        {
            DivRow(n, this.m[n, m]);
            for (int i = 0; i < this.m.GetLength(0); i++)
                if (i != n)
                    DiffRows(n, i, this.m[n, m] / this.m[i, m]);
        }
        public int GetSize(int n) 
        {
            return m.GetLength(n);
        }
        
        public double Determinant
        {
            get 
            {
                double[,] m2 = m.Clone() as double[,];
                var c = new Matrix(m2);
                var dim = this.m.GetLength(0);
                double res = 1;
                for (int i = 0; i < dim; i++)
                {
                    res *= c[i,i];
                    c.ColNormalize(i,i);
                }
                return res;
            }
        }

        public double Max_Eigenvalue(List<double> start, double eps = 0.001)
        {
            var old_iter = start;
            var iter = this * start;
            double old_ret = 0;
            double ret = iter[0]/old_iter[0];
            do
            {
                old_ret = ret;
                old_iter = iter;
                iter = this * iter;
                ret = iter[0]/old_iter[0];
            }
            while(Math.Abs(ret - old_ret) > eps);
            return ret;
        }
    }
}
