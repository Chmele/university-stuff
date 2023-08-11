using System;
using System.Collections.Generic;
using System.Text;
using ChMLab1.Interfaces;

namespace ChMLab1
{
    class JacobiMethod : MatrixMethod
    {
        public JacobiMethod(double precision) : base(precision) { }

        public JacobiMethod(double precision, ILogger logger) : base(precision, logger) { }

        public override List<double> Iterate(SLE m, List<double> answers)
        {
            var newAnswers = new List<double>(answers);
            for(int i = 0; i < m.Right.Count; i++)
                newAnswers[i] = Express(i, new List<double>(new List<double>(m.Left.GetRow(i))),answers,m.Right[i]);
            answers = newAnswers;
            return answers;
        }
        private double Express(int n, List<double> row, List<double> answers, double r)
        {
            double b = 0;
            for(int i = 0; i < row.Count; i++)
                if (i != n)
                    b -= (row[i]/row[n])*answers[i];
            b += r/row[n];
            return b;
        }
    }
}