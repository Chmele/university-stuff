using System;

namespace ComputerModellingLab2
{
    class Program
    {
        static void Main(string[] args)
        {
            Func<Dot, double, double> f1 = (d,t) => -2+5*d[2];
            Func<Dot, double, double> f2 = (d,t) => -(1-Math.Sin(t))*d[0] - d[1] + 3*d[2];
            Func<Dot, double, double> f3 = (d,t) => -d[0] + 2*d[2];

            var sys = new DiffEquationSystem(f1, f2, f3);

            var p = new Problem(sys, new Dot(2, 1, 1));
            
            foreach(var i in Euler.Solve(p, 0, 0.5, 0.05)){
                Console.WriteLine(i.ToString());
            }
        }
    }
}
