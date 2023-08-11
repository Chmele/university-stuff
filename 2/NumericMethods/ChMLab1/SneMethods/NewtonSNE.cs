using System;
using System.Collections.Generic;

namespace ChMLab1
{
    class NewtonSNE
    {
        public static List<double> Seek(SNE s, List<double> start, double eps = 0.001)
        {
            var old_dot = start;
            var dot = start;
            var gauss = new GaussMethod(1e-5);
            do
            {
                old_dot = new List<double>(dot);
                var sle = new SLE(s.JacobiInDot(dot), s.ValuesInDot(dot));
                var z = gauss.Seek(sle);
                for(int i = 0; i < dot.Count; i++)
                {
                    dot[i] -= z[i];
                }
            }
            while(Math.Abs(old_dot[0]-dot[0]) > eps);
            return dot;
        }
    }
}