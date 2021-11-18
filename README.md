# eth-tree
This is my first attempt at a project in the Web3 space! The idea behind it was to create an address tree explorer on the Ethereum network that, given an address, would
display all of the addresses it has had a transaction with, the amount in Wei of that transaction, and recursively do the same for all of those addresses and so on and so forth.
Right now, I've got the bare bones of it down but it's definitely not a finished product, as it does not do anything recursively and only displays the addresses associated with the
given address. This was just a project I made for fun, as well as practice - so the goal wasn't production level quality.


As you can see, it's pretty ugly right now but I'm okay with that! This is a python Flask app and has only ever been run locally,  but it is pulling these transactions from the Ethereum mainnet!


![eth-tree](https://user-images.githubusercontent.com/55170695/142483964-3bb410f9-b2a0-4358-b965-70e04283c19e.png)



![txs](https://user-images.githubusercontent.com/55170695/142484003-c5fa79a3-53eb-46f9-b1b6-2787192e0269.png)
