using System;
using System.Collections.Generic;

namespace ChMLab1.Interfaces
{
    abstract class MatrixMethod
    {
        protected double precision;
        
        public ILogger logger;
        
        public MatrixMethod(double precision)
        {
            this.precision = precision;
            this.logger = new NullLogger();
        }

        public MatrixMethod(double precision, ILogger logger)
        {
            this.precision = precision;
            this.logger = logger;
        }

        public List<double> Seek(SLE m, List<double> answers)
        {
            while (!Stop(m, answers))
            {
                logger.Log(answers);
                answers = Iterate(m,answers);
            }
            return answers;
        }
        public List<double> SeekIterations(SLE m, List<double> answers, int n)
        {
            for (int i = 0; i < n; i++)
            {
                logger.Log(answers);
                answers = Iterate(m, answers);
            }
            return answers;
        }
        protected bool Stop(SLE m, List<double> answers)
        {
            var newAnswers = new List<double>(Iterate(m,answers));
            for (int i = 0; i < m.Right.Count; i++)
            {
                if (Math.Abs(answers[i]-newAnswers[i]) >= precision)
                    return false;
            }
            return true;
        }
        abstract public List<double> Iterate(SLE m, List<double> answers);
    }
}
