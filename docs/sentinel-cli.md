# sentinel-cli [command] 

All basic commands for creating objects:

## User Creation

<pre>
#How to create evan on the network
--create="user" --name="blockchain-proposal-evan-2016" --revision=1 --subclass="(option)" --darksilk_monthly=233.32 --first_name="evan" --last_name="duffield"
--address1="123 w. main ave" --address2="#123" --city="Phoenix" --state="Arizona" --country="US"
</pre>

### Subclass Options
<pre>
--subclass="employer" : Someone mananging a project
--subclass="employee" : Someone working on a project
</pre>

## Voting
<pre>
--name="blockchain-proposal-evan-2016" --vote-times=22 --vote-type="funding" --vote-outcome="yes"
</pre>

## Expense
<pre>
--name="expense-darksilkcon-japan-2018" --amount=2.2342 --desc="Flight to Japan, for DarkSilk-CON 2018"
</pre>

Expenses are required to be things required to do your job. They can be things like plane tickets, advertising costs, webservers, debugging hardware, etc. 
