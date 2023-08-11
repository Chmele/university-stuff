using System;

namespace ComputerModelling
{
    public static class RungeRule
    {
        public static double Delta(IIntegrateStrategy method, double old_res, double res)
        {
            var theta = method.GetRungeTheta();
            return theta * Math.Abs(res - old_res);
        }
    }
}