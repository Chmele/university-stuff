using System;
using System.Collections.Generic;
using System.Text;

namespace ChMLab1
{
    class SLE
    {
        private Matrix left;
        private List<double> right;
        public Matrix Left{get=>left; set=>left = value;}
        public List<double> Right{get=>right; set=> right = value;}
        public double this[int n, int m] => this.left[n,m];
        public double this[int n] => this.right[n];
        public SLE(Matrix m, List<double> v)
        {
            left = m;
            right = v;
        }
        public void ColNormalize(int n, int m)
        {
            right[n] /= this[n, m];
            left.DivRow(n, this[n, m]);
            for (int i = 0; i < this.left.GetSize(0); i++)
                if (i != n)
                {
                    var k = this[n, m] / this[i, m];
                    right[i] -= right[n] / k;
                    left.DiffRows(n, i, k);
                }
        }
    }
}
