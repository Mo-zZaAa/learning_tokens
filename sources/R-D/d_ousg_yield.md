> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ondo.finance/llms.txt
> Use this file to discover all available pages before exploring further.

# Yield

### **How does OUSG earn yield?**

The OUSG portfolio is invested in funds issued by leading asset managers such as BlackRock, Franklin Templeton, WisdomTree, Fidelity, and others, along with bank deposits and USDC for liquidity purposes. You can view an overview of the current portfolio [here](https://ondo.finance/ousg#:~:text=Partners-,Portfolio%20Overview,-As%20of%20November). The portfolio may, in the future, include other US Treasury funds and/or direct investments in US Treasuries. As these investments accrue yield daily, we recognized this yield by increasing the Net Asset Value (NAV) of the underlying fund, thereby increasing the NAV per OUSG token.

### **How long after investing do I start earning yield/interest?**

Since yield is effectively incorporated into the price of OUSG whenever we update the price of OUSG onchain, you start earning yield either the day of your subscription or the next, according to whether you subscribed before or after the price update for the day.

The only exceptions to this are weekends and holidays, since the next price update will not happen until the next Business Day. For example, say you subscribe on Friday after the price update. Since the next price update after that will not happen until Monday, the yield earned on Saturday and Sunday will not be reflected in the token price until the price is updated on Monday.

### **How frequently (and when) do you update the onchain OUSG token price (NAV)?**

We typically update the price once every Business Day. We typically aim to do this sometime between 4-6pm ET but, because this is a manual process, it may sometimes take longer.

### **How often does OUSG pay out yield?**

We aim to pay out yield every Business Day based on the [net income received](https://docs.ondo.finance/qualified-access-products/ousg/yield.md#how-is-the-amount-of-yield-determined).

In the event that we are unable to update the price or rebase on a given Business Day, investors holding their tokens will still receive the yield from the 'missed' day at the time of the next update. Note that tokenholders who submit a redemption request prior to a price update or rebase on a given day are not paid yield on those tokens for that day. Please also note yield is paid to the holder of the tokens at the time of update; if you have already transferred or redeemed your tokens, you will not receive yield on them. Note that OUSG holders are not 'paid out' yield per se; instead, that yield is reinvested into fund, thereby increasing the value of their *existing* OUSG tokens.

### **How is the amount of yield determined?**

The amount of yield paid out on a given day is based upon the Net Income received as of the end of the previous Business Day. This Net Income is then allocated ratably across all OUSG holders (e.g. if you held 100% of the OUSG tokens, you'd be allocated 100% of the net income; if you held 25% of the OUSG tokens, you'd be allocated 25% of the net income, etc).

To ensure timely price updates, each Business Day the Fund makes a conservative estimate of the Net Income it expects to receive for the day (including, if immediately followed by a weekend or holiday, any income it expects to accrue to it over those non-business days) based upon historical data. When the Fund then receives final information on the actual income received from its holdings, it makes an additional adjustment to its Net Income on the following Business Day. It does this in order to provide more consistent updates to the OUSG price.

### **When is the APY updated and how is it calculated?**

The APY on our [website](https://ondo.finance/ousg) is generally updated each weekday, excluding holidays. APY is calculated based on the average income, net of expenses, earned over the 30 calendar days preceding and including the day that APY is updated. This yield reflects past performance. Past performance is not indicative of future results. Actual yields may vary depending on market conditions and other factors.

The formula used to calculate the APY is `APY = e^((End NAV - Start NAV) / (30/365)) - 1`

### **When are the 7-Day Yield and 30-Day Yield updated, and how are they calculated?**

The yields on our [website](https://ondo.finance/ousg) are generally updated each weekday, excluding holidays. 7-Day Yield is calculated based on the average income, net of expenses, earned over the 7 calendar days preceding and including the day that the 7-Day Yield is updated. 30-Day Yield is calculated based on the average income, net of expenses, earned over the 30 calendar days preceding and including the day that the 30-Day Yield is updated. These yields reflect past performance. Past performance is not indicative of future results. Actual yields may vary depending on market conditions and other factors.

The formulas used to calculate the 7-Day Yield and 30-Day Yield are:

* `7-Day Yield = e^((End NAV - Start NAV) / (7/365)) - 1`
* `30-Day Yield = e^((End NAV - Start NAV) / (30/365)) - 1`


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.