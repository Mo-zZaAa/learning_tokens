---
url: https://support.kraken.com/articles/11695305309204-example-rest-api-request-using-bash
title: Example REST API request using bash | Kraken
description: Support Center for Kraken.com | Bitcoin & Cryptocurrency Exchange | Bitcoin Trading Platform
fetched: 2026-11-16
method: static
plan: skim
---

Ask AI

All

Filter by:

Select Product

How do I deposit cash into my account?

I need help with account verification

Why can't I access my account?

Are there any crypto withdrawal fees?

I need help signing into my account

1. [Support](/)
2. [Trading](/categories/200187143-trading)
3. [API](/sections/4402371110548-api)
4. [Example API Code](/sections/360003946512-example-api-code)
5. [REST and WebSocket code examples](/sections/10033754515604-rest-and-websocket-code-examples)

# Example REST API request using bash

Last updated: March 31, 2025

### Introduction

Implementing a [Kraken REST API](https://docs.kraken.com/rest/) interface using the [Bourne Again shell (bash)](https://en.wikipedia.org/wiki/Bash_(Unix_shell)) and some associated commands (openssl, base64, xxd, etc.) can be a convenient and efficient solution for interacting with Kraken's markets (although it would not be the fastest implementation compared to compiled code).

Bash and the required commands are readily available (pre-installed) on most UNIX, Linux, and macOS systems, and can be easily installed on Windows and other systems, so all of the required software is available without using any additional third party API tools or libraries.

Using a plain text editor (even an old school editor such as [vi](https://en.wikipedia.org/wiki/Vi)) and a few lines of code, it is possible to access both public market data and private account data, and also to place/cancel orders on Kraken's markets.

### Example Code

The following code shows a bash code implementation for calling the REST API **Balance** endpoint:

#!/usr/bin/env bash  
  
# API public/private keys copied from account management web site  
  
api\_key='gxTXpC4Ag/N0QPKlYnRhL1qVB2G/HZV1eB2drl7eOXga30dEKoB+EUMs'  
api\_private='62kRfRX7BI8G8T/jl7clnZ+vSfJt7YmQN23JQkJfHCE6oxecJX4fN4i2RitmRhyFzfJ4efKy2yCo4H068rfv0A=='  
  
# API variables (URL, endpoint, nonce, etc.)  
  
api\_host='https://api.kraken.com'  
api\_endpoint='/0/private/Balance'  
api\_nonce=`date +%s`  
api\_post="nonce=$api\_nonce"  
  
# Authentication algorithm (SHA256 and HMAC SHA512)  
  
api\_private\_hex=`echo -n $api\_private base64 -d xxd -p tr -d "\n"`  
echo -n $api\_endpoint > kapi\_bash.bin  
echo -n $api\_nonce$api\_post openssl dgst -sha256 -binary >> kapi\_bash.bin  
api\_sign=`cat kapi\_bash.bin openssl dgst -binary -sha512 -mac HMAC -macopt hexkey:$api\_private\_hex base64`  
  
# HTTP request (POST)  
  
curl --header "API-Key: $api\_key" --header "API-Sign: $api\_sign" --data $api\_post $api\_host$api\_endpoint

and the matching code can also be [downloaded (as a kapi\_bash.sh file)](/article_attachments/13502947262356).

### Further Use/Development

To retrieve your own account balances, the example API key should be replaced with an API key from your own Kraken account, and additional API endpoints can be enabled simply by modifying the api\_endpoint variable and the api\_post variable (if needed).

[Introduction](#2a4-introduction)[Example Code](#738-example-code)[Further Use/Development](#b02-further-usedevelopment)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@graph":[{"@type":"WebSite","url":"https://kraken.com","description":"Buy, sell, trade and learn about crypto on Kraken — the simple, powerful crypto platform that grows with you.","potentialAction":{"@type":"RegisterAction","target":"https://www.kraken.com/sign-up"},"publisher":{"@context":"https://schema.org","@type":"Organization","name":"Kraken","alternateName":"Kraken Exchange","url":"https://www.kraken.com/","logo":{"@type":"ImageObject","@id":"https://assets.kraken.com/marketing/static/kraken-logo.jpg","url":"https://assets.kraken.com/marketing/static/kraken-logo.jpg","contentUrl":"https://assets.kraken.com/marketing/static/kraken-logo.jpg","width":900,"height":900,"caption":"Kraken"},"image":{"@id":"https://assets.kraken.com/marketing/static/kraken-logo.jpg"},"sameAs":["https://www.facebook.com/KrakenFX","https://twitter.com/krakenfx","https://www.youtube.com/@KrakenCryptoExchange","https://en.wikipedia.org/wiki/Kraken_(company)","https://www.linkedin.com/company/krakenfx","https://www.instagram.com/krakenfx/","https://www.reddit.com/r/Kraken","https://apps.apple.com/us/app/kraken-buy-crypto-bitcoin/id1481947260","https://play.google.com/store/apps/details?id=com.kraken.invest.app&hl=en_US"],"contactPoint":{"@type":"ContactPoint","url":"https://support.kraken.com/hc/en-us/forms","contactType":"Customer Service"},"address":{"@type":"PostalAddress","streetAddress":"237 Kearny St #102","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94108","addressCountry":"US"}}},{"@type":"BreadcrumbList","@id":"https://support.kraken.com/articles/11695305309204-example-rest-api-request-using-bash#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Kraken.com","item":"https://support.kraken.com/"},{"@type":"ListItem","position":2,"name":"Articles","item":"https://support.kraken.com/articles"},{"@type":"ListItem","position":3,"name":"11695305309204 Example Rest Api Request Using Bash","item":"https://support.kraken.com/articles/11695305309204-example-rest-api-request-using-bash"}]},{"@type":"WebPage","@id":"https://support.kraken.com/articles/11695305309204-example-rest-api-request-using-bash#webpage","url":"https://support.kraken.com/articles/11695305309204-example-rest-api-request-using-bash","name":"Example REST API request using bash | Kraken","description":"Support Center for Kraken.com | Bitcoin & Cryptocurrency Exchange | Bitcoin Trading Platform","isPartOf":{"@id":"https://support.kraken.com/#website"},"publisher":{"@id":"https://support.kraken.com/#organization"},"breadcrumb":{"@id":"https://support.kraken.com/articles/11695305309204-example-rest-api-request-using-bash#breadcrumb"}}]}
{"@context":"https://schema.org","@graph":[{"@type":"Article","headline":"Example REST API request using bash","articleBody":"—  Introduction \n\nImplementing a Kraken REST API interface using the Bourne Again shell (bash) and some associated commands (openssl, base64, xxd, etc.) can be a convenient and efficient solution for interacting with Kraken's markets (although it would not be the fastest implementation compared to compiled code).Bash and the required commands are readily available (pre-installed) on most UNIX, Linux, and macOS systems, and can be easily installed on Windows and other systems, so all of the required software is available without using any additional third party API tools or libraries.Using a plain text editor (even an old school editor such as vi) and a few lines of code, it is possible to access both public market data and private account data, and also to place/cancel orders on Kraken's markets.\n—  Example Code \n\nThe following code shows a bash code implementation for calling the REST API Balance endpoint:#!/usr/bin/env bash\n\n# API public/private keys copied from account management web site\n\napi_key='gxTXpC4Ag/N0QPKlYnRhL1qVB2G/HZV1eB2drl7eOXga30dEKoB+EUMs'\napi_private='62kRfRX7BI8G8T/jl7clnZ+vSfJt7YmQN23JQkJfHCE6oxecJX4fN4i2RitmRhyFzfJ4efKy2yCo4H068rfv0A=='\n\n# API variables (URL, endpoint, nonce, etc.)\n\napi_host='https://api.kraken.com'\napi_endpoint='/0/private/Balance'\napi_nonce=`date +%s`\napi_post=\"nonce=$api_nonce\"\n\n# Authentication algorithm (SHA256 and HMAC SHA512)\n\napi_private_hex=`echo -n $api_private | base64 -d | xxd -p | tr -d \"\\n\"`\necho -n $api_endpoint > kapi_bash.bin\necho -n $api_nonce$api_post | openssl dgst -sha256 -binary >> kapi_bash.bin\napi_sign=`cat kapi_bash.bin | openssl dgst -binary -sha512 -mac HMAC -macopt hexkey:$api_private_hex | base64`\n\n# HTTP request (POST)\n\ncurl --header \"API-Key: $api_key\" --header \"API-Sign: $api_sign\" --data $api_post $api_host$api_endpoint\nand the matching code can also be downloaded (as a kapi_bash.sh file).\n—  Further Use/Development \n\nTo retrieve your own account balances, the example API key should be replaced with an API key from your own Kraken account, and additional API endpoints can be enabled simply by modifying the api_endpoint variable and the api_post variable (if needed).","datePublished":"2025-03-31T00:00:00.000Z","wordCount":289,"timeRequired":"PT2M"}]}
```