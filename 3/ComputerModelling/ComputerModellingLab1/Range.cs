using System.Collections.Generic;

namespace ComputerModelling
{
    public class Range
    {
        private double a;
        private double b;
        public double A { get => a; }
        public double B { get => b; }
        public double Length { get => b - a; }
        public Range(double left, double right)
        {
            this.a = left;
            this.b = right;
        }
        public List<Range> SplitBy(int n)
        {
            var ret = new List<Range>();
            for (int i = 0; i < n; i++)
                ret.Add(new Range(a + ((double)i / n) * (b - a), a + ((double)(i + 1) / n) * (b - a)));
            return ret;
        }
    }
}