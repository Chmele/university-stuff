using System;
using System.Collections.Generic;

namespace ChMLab1
{
    //system of nonlinear equations
    class SNE
    {
        List<Func<List<double>,double>> functions = new List<Func<List<double>,double>>();
        Func<List<double>,double>[,] jacobiMatrix = { };
        
        public SNE(List<Func<List<double>,double>> funcs, Func<List<double>,double>[,] jm)
        {
            this.functions = funcs;
            this.jacobiMatrix = jm;
        }


        public Matrix JacobiInDot(List<double> dot)
        {
            double[,] m = new double[dot.Count, dot.Count];
            for(int i = 0; i < jacobiMatrix.GetLength(0); i++)
            {
                for(int j = 0; j < jacobiMatrix.GetLength(1); j++)
                    m[i,j] = jacobiMatrix[i,j](dot);
            }
            return new Matrix(m);
        }

        public List<double> ValuesInDot(List<double> dot)
        {
            var r = new List<double>();
            foreach(Func<List<double>,double> f in functions)
            {
                r.Add(f(dot));
            }
            return r;
        }
    } 

}