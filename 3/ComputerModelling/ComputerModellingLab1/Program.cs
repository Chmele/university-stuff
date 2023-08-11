using System;

namespace ComputerModelling
{
    class Program
    {
        static void Main(string[] args)
        {

            Func<double, double> f = x => 1 / (1 + Math.Pow(x, 3));
            Range r = new Range(2, 100);
            r.SplitBy(2);
            var p = new Problem(f, r, 0.005);
            var method = new LeftRectangleMethod();
            Console.WriteLine(p.Integrate(method));
        }
    }
}
