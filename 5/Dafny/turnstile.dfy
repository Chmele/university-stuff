class Turnstile {
    var isOpen: bool;
    var passengersPassed: nat;
    var price: nat;

    constructor(price: nat)
    ensures !this.isOpen
    {
        this.isOpen := false;
        this.passengersPassed := 0;
        this.price := price;
    }

    method pay(card: Card)
    modifies this
    modifies card
    requires !this.isOpen
    requires card.amount >= this.price
    ensures this.isOpen
    {
        card.charge(this.price);
        this.isOpen := true;
    }

    method passed()
    modifies this
    requires this.isOpen
    {
        this.isOpen := false;
    }
}

class Card {
    var amount: nat

    constructor()
    {
        this.amount := 0;
    }

    method charge(amount: nat)
    modifies this
    ensures this.amount == old(this.amount) + amount
    {
        this.amount := this.amount + amount;
    }

    method discharge(amount: nat)
    modifies this
    requires amount <= this.amount
    ensures this.amount == old(this.amount) - amount
    {
        this.amount := this.amount - amount;
    }
}

class Passenger {
    var card: Card;
    var passedTurnstile: bool;

    constructor()
    ensures fresh(card)
    {
        this.card := new Card();
        this.passedTurnstile := false;
    }

    method pay(t: Turnstile)
    modifies this.card
    modifies t
    requires !t.isOpen
    requires this.card.amount >= t.price
    ensures this.card == old(this.card)
    ensures t.isOpen
    {
        t.pay(this.card);
    }

    method pass(t: Turnstile)
    modifies this
    modifies t
    requires t.isOpen
    ensures this.passedTurnstile
    {
        t.passed();
        this.passedTurnstile := true;
    }   
}

method Main() 
    {
        var p := new Passenger();
        var price := 8;
        var turnstile := new Turnstile(price);
        p.card.charge(8);
        if p.card.amount >= turnstile.price{
            p.pay(turnstile);
            p.pass(turnstile);
        }
    }