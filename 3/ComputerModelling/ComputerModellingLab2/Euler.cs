using System.Collections.Generic;

namespace ComputerModellingLab2
{
    public static class Euler
    {
        public static List<Dot> Solve(Problem p, double start, double end, double step){
            var t = start;
            var ret = new List<Dot>();
            var current_dot = p.Start;
            while (t <= end){
                t += step;
                ret.Add(current_dot);
                current_dot += p.EvalInDot(current_dot, t) * step;
            }
            return ret;
        }
    }
}