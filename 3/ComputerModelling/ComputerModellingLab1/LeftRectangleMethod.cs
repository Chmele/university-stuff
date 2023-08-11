namespace ComputerModelling
{
    public class LeftRectangleMethod : IIntegrateStrategy
    {
        public double GetRungeTheta() { return (double)1 / 3; }
        public double Integrate(Problem p)
        {
            int i = 50;
            double old_res;
            double res = Iteration(p, i);
            do
            {
                old_res = res;
                i *= 2;
                res = Iteration(p, i);
            } while (RungeRule.Delta(this, old_res, res) > p.Eps);
            return res;
        }

        private double Iteration(Problem problem, int range_amount)
        {
            var rangeList = problem.Range.SplitBy(range_amount);
            double ret = 0;
            foreach (var r in rangeList)
                ret += problem.Func(r.A) * (r.Length);
            return ret;
        }
    }
}