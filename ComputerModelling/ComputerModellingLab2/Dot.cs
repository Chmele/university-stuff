using System.Collections.Generic;

namespace ComputerModellingLab2
{
    public class Dot
    {
        private List<double> coords;

        public Dot(List<double> l){
            this.coords = l;
        }

        public Dot(params double[] numbers){
            this.coords = new List<double>();
            foreach(var i in numbers){
                coords.Add(i);
            }
        }

        public double this[int n] => this.coords[n];

        public string ToString(){
            var ret = "";
            foreach(var i in coords){
                ret += $"{i.ToString(), 20}" + " ";
            }
            return ret;
        }

        public static Dot operator+(Dot a, Dot b){
            var l = new List<double>();
            for(int i = 0; i < a.coords.Count; i++){
                l.Add(a.coords[i]+b.coords[i]);
            }
            return new Dot(l);
        }
        
        public static Dot operator*(Dot a, double n){
            var l = new List<double>();
            foreach(var i in a.coords){
                l.Add(i * n);    
            }
            return new Dot(l);
        }
    }
}