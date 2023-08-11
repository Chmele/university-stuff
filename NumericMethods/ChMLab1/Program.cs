using System;
using System.Collections.Generic;

namespace ChMLab1
{
    class Program
    {
        static void Main(string[] args)
        {
            var a = new double[,] {
                {1,2,3},
                {2,3,4},
                {3,4,5}
            };
            var m = new Matrix(a);
            var start = new List<double>{1,1,1};
            Console.WriteLine(m.Max_Eigenvalue(start));
            // var f1 = new Func<List<double>,double>((d) => Math.Sin(d[0]) + 2*d[1] - 1.6);
            // var f2 = new Func<List<double>,double>((d) => Math.Cos(d[1]-1) - 1);

            // var j11 = new Func<List<double>,double>((d) => Math.Cos(d[0]) + 2*d[1]);
            // var j12 = new Func<List<double>,double>((d) => Math.Sin(d[0]) + 2);
            // var j21 = new Func<List<double>,double>((d) => 0);
            // var j22 = new Func<List<double>,double>((d) => -Math.Sin(d[1]-1));

            // var functions = new List<Func<List<double>,double>>{f1,f2};
            // var jacobi = new Func<List<double>,double>[,]{
            //     {j11,j12},
            //     {j21,j22}
            // };

            // var sne = new SNE(functions, jacobi);
            // var start = new List<double> { 0.5, 0.5};
            // var ans = NewtonSNE.Seek(sne, start);
            // foreach(double k in ans)
            // {
            //    Console.WriteLine(k);
            // }
            // Console.WriteLine(f1(ans));
            // Console.WriteLine(f2(ans));
        }
    }
}
