> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ondo.finance/llms.txt
> Use this file to discover all available pages before exploring further.

# Token Quote & Pricing

> How a portfolio token's price is determined and how quotes work.

### How is the price of an Ondo Intelligent Portfolio token determined?

The price of a portfolio token reflects the weighted value of its constituent assets. Each token is backed by a basket of Ondo tokenized stocks and ETFs, plus any cash in transit, shown as a per-token value:

Price per token = (sum (constituent token price × quantity held) + cash in transit) ÷ total portfolio tokens outstanding

Because each constituent is itself an Ondo tokenized stock and a total-return tracker, dividends on the underlying assets are reinvested at the constituent token level (net of any applicable [withholding taxes](https://docs.ondo.finance/ondo-stocks/fees-and-taxes.md)) and reflected in each constituent's price. That total return flows through to the portfolio token's price automatically. The portfolio token therefore reflects both price movements *and* reinvested income across every asset in the basket.

### Can you give me an example?

Let's take a simplified portfolio, SAMPLEon, holding two Ondo tokenized stocks at 50% each. At inception, assume the basket backing one portfolio token is worth \$100 — \$50 of Token A and \$50 of Token B.

If Token A rises 10% and Token B is unchanged, the basket is now worth \$105, so the portfolio token's price is \$105.

Dividends work the same way, because each constituent is itself a total-return tracker. When the stock underlying Token A pays a dividend, that dividend is reinvested at the constituent level (net of applicable withholding taxes) and reflected in Token A's price — the same way all Ondo tokenized stocks work. The portfolio simply holds Token A, so the increase flows through to the portfolio token's price automatically. There is no separate dividend handling at the portfolio level, and there is never anything for you to claim or reinvest.

Over time, this means the price of a portfolio token reflects the total return of the full basket — including price movements and reinvested income across every constituent. Current holdings and per-token value are shown on each portfolio's product page at [app.ondo.finance](https://app.ondo.finance).

### What is a total-return tracker?

Total-return trackers are financial assets that are designed to mirror the complete performance of an index or asset. Unlike *price* return trackers, which only capture an asset's market value changes, *total* return trackers account for all cash flows — dividends, interest, or capital gains distributions — assuming these are reinvested to compound returns (net of applicable withholding taxes).

A total-return tracker includes:

* Price movements – gains or losses in the assets' market value
* Income distributions – such as dividends (for stocks) or interest (for bonds)
* Corporate actions – like mergers that may affect total value

By capturing both capital gains and income, total-return trackers offer a more comprehensive reflection of performance than price-only trackers.

### When I am actually buying or selling a portfolio token, the quoted price seems to be slightly different from the chart price on the product page. Why?

When you indicate that you want to buy or sell a portfolio token, we provide you a quote for a price that's guaranteed for some amount of time. To generate that quote, the platform automatically looks at existing inventory, market conditions, and other factors and then does a little bit of (proprietary) math to figure out what an appropriate quote price should be for that order.

For a portfolio token, that quote accounts for the cost of buying or selling *every asset in the portfolio's basket*, each of which has its own bid-ask spread in the underlying market. The "main" price you see on the price chart of the product page is our estimate of the per-token value of the portfolio's holdings, whereas the quote price is the result of our proprietary method for determining at what price we can guarantee we can buy or sell that number of tokens across the full basket. Those numbers should never be *too* different from one another, but that's where the discrepancy comes from.

(Please note that if you are buying a portfolio token on the secondary market, whomever you are transacting with may be charging their own fees. You are also responsible for your own gas costs.)

### Is there price history from before a portfolio's launch?

Each portfolio's live price data starts from its inception date. Where a portfolio token's pre-inception price performance is shown, it is hypothetical, based on backtesting, and clearly labeled as such — it does not represent actual results. Performance after inception reflects actual results. Past performance, whether actual or hypothetical, does not guarantee future results.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.