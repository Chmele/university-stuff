class Mark{
    var numerical: nat;
    var national: nat;

    constructor (num: nat)
    requires 0 <= num <= 100
    ensures 2 <= this.national <= 5
    {
        if 0 <= num < 60
        {
            this.national := 2;
        }
        else if 60 <= num < 75
        {
            this.national := 3;
        }
        else if 75 <= num < 90
        {
            this.national := 4;
        }
        else if 90 <= num <= 100
        {
            this.national := 5;
        }
        this.numerical := num;
    }
}

method Main()
{
    var mark := new Mark(100);
}