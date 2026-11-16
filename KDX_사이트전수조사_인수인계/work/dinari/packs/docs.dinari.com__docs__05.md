# 읽기 묶음: docs.dinari.com / docs (5/5)


<<<PAGE https://docs.dinari.com/docs/managing-kyc>>>
---
url: https://docs.dinari.com/docs/managing-kyc
title: Identity Verification (KYC)
description: Requirements In order to comply with international and domestic regulations, all entities require identity verification (KYC). This can be done in a couple ways, via Partner KYC (also known as KYC reliance) and Managed KYC (Dinari-managed). Integration Types Partner KYC If you already collect and ve…
fetched: 2026-11-16
method: static
plan: read
---

## Getting Started

* [Quickstart](https://docs.dinari.com/docs/quickstart)
* [Deploy to production](https://docs.dinari.com/docs/deploy-to-production)
* [Hosted Trading](https://docs.dinari.com/docs/hosted-trading)

## Core Concepts

* [What are dShares™?](https://docs.dinari.com/docs/what-is-dshare)
  + [Blockchain](https://docs.dinari.com/docs/blockchain)
    - [Wrapping dShares™](https://docs.dinari.com/docs/wrapping)
    - [Hyperliquid](https://docs.dinari.com/docs/hyperliquid)
    - [dShare Bridging Guide](https://docs.dinari.com/docs/dshare-bridging-guide)
    - [Deprecation Notices](https://docs.dinari.com/docs/deprecations)
* [What is USD+?](https://docs.dinari.com/docs/what-is-usd)
  + [Blockchain](https://docs.dinari.com/docs/usdplus-evm)
    - [EVM](https://docs.dinari.com/docs/usdplus-evm)
      * [Integration Guide](https://docs.dinari.com/docs/usdplus-evm-integration-guide)
* [Trading Hours](https://docs.dinari.com/docs/trading-hours)
* [Partner Fees](https://docs.dinari.com/docs/fees)

## Technical Integration

* [Entity Management](https://docs.dinari.com/docs/entity-management)
  + [Identity Verification (KYC)](https://docs.dinari.com/docs/managing-kyc)
  + [Managing Accounts](https://docs.dinari.com/docs/managing-accounts)
  + [Managing Wallets](https://docs.dinari.com/docs/managing-wallets)
  + [Funding Accounts through Wallets](https://docs.dinari.com/docs/funding-accounts-through-wallets)
* [Ordering](https://docs.dinari.com/docs/placing-orders)
  + [Placing Orders](https://docs.dinari.com/docs/placing-orders)
    - [Placing dShare Orders with Alchemy](https://docs.dinari.com/docs/placing-dshare-orders-with-alchemy)
    - [Placing dShare Orders with Safe Vaults](https://docs.dinari.com/docs/placing-dshare-orders-with-safe-vaults)
  + [Order Types & Behaviors](https://docs.dinari.com/docs/order-type)
  + [Order Fulfillment Amounts in the Orders API](https://docs.dinari.com/docs/order-fulfillment-amounts-in-the-orders-api)
* [Stock Data](https://docs.dinari.com/docs/stock-data)
  + [Pricing & Quotes](https://docs.dinari.com/docs/pricing-quotes)
  + [24/7 Tradable Assets](https://docs.dinari.com/docs/24-7-trading)
  + [24/5 Tradable Assets](https://docs.dinari.com/docs/245-tradable-assets)
* [Corporate Actions](https://docs.dinari.com/docs/corporate-action-processing)
  + [Dividends](https://docs.dinari.com/docs/dividend-payments)
  + [Stock Splits](https://docs.dinari.com/docs/stock-split-handling)
  + [Ticker Changes](https://docs.dinari.com/docs/ticker-changes)
  + [Mergers](https://docs.dinari.com/docs/mergers)
* [Websockets for Order Data (BETA)](https://docs.dinari.com/docs/websockets)
* [Troubleshooting & Known Issues](https://docs.dinari.com/docs/error-codes)
  + [Error Codes](https://docs.dinari.com/docs/error-codes)
  + [Orders Stuck in SUBMITTED Status](https://docs.dinari.com/docs/stuck-orders)
  + [Smart Contract Wallet Support](https://docs.dinari.com/docs/smart-contract-wallet-support)

## Compliance and Regional

* [Security](https://docs.dinari.com/docs/security)
* [Regional Requirements](https://docs.dinari.com/docs/regional-requirements)
  + [US Customers](https://docs.dinari.com/docs/us)
* [Restrictions](https://docs.dinari.com/docs/restrictions)
* [Taxes & Reporting](https://docs.dinari.com/docs/taxes-reporting)

## Support

* [Staying Safe on Dinari](https://docs.dinari.com/docs/staying-safe-on-dinari)
* [FAQs](https://docs.dinari.com/docs/faqs)
* [Status Pages](https://docs.dinari.com/docs/status-pages)

Powered by

# Identity Verification (KYC)

# Requirements

In order to comply with international and domestic regulations, all entities require identity verification (KYC). This can be done in a couple ways, via Partner KYC (also known as KYC reliance) and Managed KYC (Dinari-managed).

## Integration Types

### Partner KYC

If you already collect and verify KYC information from your users, you may submit their KYC data to the Dinari API for a completely transparent experience for your customers.

Requirements:

* Use a [supported KYC provider](https://docs.dinari.com/docs/managing-kyc)
* Submit all the required KYC fields to the Dinari KYC API.
* Submit a copy of your AML program

> ⚠️
>
> ### KYC Policy and Process Audits
>
> Dinari may periodically request to audit your KYC policies and processes. Dinari will periodically verify the data sent to us.

To enable Partner KYC, please reach out to [[email protected]](https://docs.dinari.com/cdn-cgi/l/email-protection).

### Managed KYC

If you do not currently collect or verify KYC information, Dinari provides a whitelabel solution that you can offer to your users.

1. Use the [Create Managed KYC Check](https://docs.dinari.com/reference/createmanagedentitykycembed) endpoint to generate a unique KYC URL.
2. Present this URL to a user in your application.
3. The user then follows this link and is presented with web embedded KYC flow with our identity verification partner compatible on both mobile and desktop experiences.
4. Once they complete this flow, the user's identity is verified in realtime and will then be able to place trades.

Additional fees may apply.

## Supported Identity Verification Providers

The following identity verification providers have been approved for use. If you use one that is not on this list, please let us know!

* [Persona](https://withpersona.com/)
* [Onfido/Entrust](https://www.entrust.com/)
* [Sumsub](https://sumsub.com/)
* [Plaid - Identity Verification](https://plaid.com/products/identity-verification)
* [Stripe - Identity](https://stripe.com/identity)
* [Veriff Identity Verification](https://www.veriff.com/product/identity-verification-platform)

## ⚠️ Special Jurisdictions

* US - Additional requirements apply. See the US Integration Guide at [US Customers](https://docs.dinari.com/docs/us)

# Integration

The following section details how you can manage this information. Please note that for your organization's `Entity`, the requirement is to be KYB'ed.

## SDK Reference

| Language | URL |
| --- | --- |
| Javascript / Typescript | [https://github.com/dinaricrypto/dinari-api-sdk-typescript/blob/main/reference.md#kyc](https://github.com/dinaricrypto/dinari-api-sdk-typescript/blob/main/reference.md) |
| Python | [https://github.com/dinaricrypto/dinari-api-sdk-python/blob/main/reference.md#kyc](https://github.com/dinaricrypto/dinari-api-sdk-python/blob/main/reference.md) |
| Go | [https://github.com/dinaricrypto/dinari-api-sdk-go/blob/main/reference.md#kyc](https://github.com/dinaricrypto/dinari-api-sdk-go/blob/main/reference.md) |
| Java | [https://github.com/dinaricrypto/dinari-api-sdk-java/blob/main/reference.md#kyc](https://github.com/dinaricrypto/dinari-api-sdk-java/blob/main/reference.md) |

## SDK Examples

### Partner-Managed KYC

TypeScriptPythonGoJava

```
import { createReadStream } from "node:fs";
import { DinariClient, DinariEnvironment } from "@dinari/api-sdk";

const client = new DinariClient({
  apiKeyId: process.env.DINARI_API_KEY_ID!, // This is the default and can be omitted
  apiSecretKey: process.env.DINARI_API_SECRET_KEY!, // This is the default and can be omitted
  environment: DinariEnvironment.Sandbox, // defaults to DinariEnvironment.Production
});

async function main() {
  const entity = await client.entities.createEntities({
    name: "Jane Doe",
  });

  const kyc = await client.kyc.createEntityKyc({
    entityId: entity.id,
    body: {
      jurisdiction: "BASELINE",
      data: {
        countryCode: "US",
        firstName: "Jane",
        middleName: "Marie",
        lastName: "Doe",
        birthDate: "1990-01-01",
        email: "[email protected]",
        taxIdNumber: "123-45-6789",
        addressStreet1: "123 Main St",
        addressStreet2: "Apt 4B",
        addressCity: "New York",
        addressSubdivision: "New York",
        addressPostalCode: "10001",
        addressCountryCode: "US",
      },
      providerName: "your-kyc-provider", // Name of the provider that performed the KYC
    },
  });

  // Replace with your actual document file
  const uploadResponse = await client.kyc.createEntityKycDocument({
    entityId: entity.id,
    kycId: kyc.id,
    documentType: "GOVERNMENT_ID",
    file: createReadStream("./gov-id.jpeg"),
  });

  console.log(uploadResponse);
}

main();
```

```
import datetime
import os

from dinari_api_sdk import BaselineKycCheckDataV0, CreateKycInput_Baseline, DinariClient
from dinari_api_sdk.environment import DinariClientEnvironment

client = DinariClient(
    api_key_id=os.environ["DINARI_API_KEY_ID"],  # This is the default and can be omitted
    api_secret_key=os.environ["DINARI_API_SECRET_KEY"],  # This is the default and can be omitted
    environment=DinariClientEnvironment.SANDBOX,  # defaults to DinariClientEnvironment.PRODUCTION
)

entity = client.entities.create_entities(
    name="Jane Doe",
)

kyc = client.kyc.create_entity_kyc(
    entity_id=entity.id,
    request=CreateKycInput_Baseline(
        data=BaselineKycCheckDataV0(
            country_code="US",
            first_name="Jane",
            middle_name="Marie",
            last_name="Doe",
            birth_date=datetime.date(1990, 1, 1),
            email="[email protected]",
            tax_id_number="123-45-6789",
            address_country_code="US",
        ),
        provider_name="your-kyc-provider",  # Name of the provider that performed the KYC
    ),
)

with open("./gov-id.jpeg", "rb") as f:  # Replace with your actual document file
    upload_response = client.kyc.create_entity_kyc_document(
        entity_id=entity.id,
        kyc_id=kyc.id,
        document_type="GOVERNMENT_ID",
        file=f,
    )
print(upload_response)
```

```
package main

import (
	"context"
	"fmt"
	"log"
	"os"
	"time"

	dinari "github.com/dinaricrypto/dinari-api-sdk-go"
	client "github.com/dinaricrypto/dinari-api-sdk-go/client"
	option "github.com/dinaricrypto/dinari-api-sdk-go/option"
)

func main() {
	c := client.NewDinariClient(
		option.WithBaseURL(dinari.Environments.Sandbox), // Defaults to production when omitted
		option.WithAPIKeyID(os.Getenv("DINARI_API_KEY_ID")),
		option.WithAPISecretKey(os.Getenv("DINARI_API_SECRET_KEY")),
	)

	entity, err := c.Entities.CreateEntities(context.Background(), &dinari.CreateEntityInput{
		Name: "Jane Doe",
	})
	if err != nil {
		log.Fatalf("Failed to create entity: %v", err)
	}

	birthDate := time.Date(1990, 1, 1, 0, 0, 0, 0, time.UTC)
	kyc, err := c.Kyc.CreateEntityKyc(context.Background(), &dinari.CreateEntityKycRequest{
		EntityID: entity.ID,
		Body: &dinari.CreateKycInput{
			Baseline: &dinari.CreateBaselineKycInput{
				Data: &dinari.BaselineKycCheckDataV0{
					CountryCode:        "US",
					FirstName:          dinari.String("Jane"),
					MiddleName:         dinari.String("Marie"),
					LastName:           "Doe",
					BirthDate:          &birthDate,
					Email:              dinari.String("[email protected]"),
					TaxIDNumber:        dinari.String("123-45-6789"),
					AddressStreet1:     dinari.String("123 Main St"),
					AddressStreet2:     dinari.String("Apt 4B"),
					AddressCity:        dinari.String("New York"),
					AddressSubdivision: dinari.String("New York"),
					AddressPostalCode:  dinari.String("10001"),
					AddressCountryCode: "US",
				},
				ProviderName: "your-kyc-provider", // Name of the provider that performed the KYC
			},
		},
	})
	if err != nil {
		log.Fatalf("Failed to submit KYC data: %v", err)
	}

	file, err := os.Open("./gov-id.jpeg") // Replace with your actual document file
	if err != nil {
		log.Fatalf("Failed to open file: %v", err)
	}
	defer file.Close()

	uploadResp, err := c.Kyc.CreateEntityKycDocument(context.Background(), &dinari.CreateKycDocumentFileInput{
		EntityID:     entity.ID,
		KycID:        kyc.GetBaseline().ID,
		DocumentType: dinari.KycDocumentTypeGovernmentID,
		File:         dinari.NewFileParam(file, "gov-id.jpeg", "image/jpeg"),
	})
	if err != nil {
		log.Fatalf("Failed to upload KYC document: %v", err)
	}

	fmt.Printf("Document upload response: %+v\n", uploadResp)
}
```

```
import com.dinari.api.DinariClient;
import com.dinari.api.core.Environment;
import com.dinari.api.resources.entities.requests.CreateEntityInput;
import com.dinari.api.resources.kyc.requests.CreateEntityKycRequest;
import com.dinari.api.resources.kyc.requests.CreateKycDocumentFileInput;
import com.dinari.api.types.BaselineKycCheckDataV0;
import com.dinari.api.types.CreateBaselineKycInput;
import com.dinari.api.types.CreateKycInput;
import com.dinari.api.types.KycDocumentType;
import java.io.File;

public class Main {
    public static void main(String[] args) {
        DinariClient client = DinariClient.builder()
                .environment(Environment.SANDBOX) // defaults to Environment.PRODUCTION
                .apiKeyId(System.getenv("DINARI_API_KEY_ID")) // This is the default and can be omitted
                .apiSecretKey(System.getenv("DINARI_API_SECRET_KEY")) // This is the default and can be omitted
                .build();

        var entity = client.entities().createEntities(
                CreateEntityInput.builder().name("Jane Doe").build());

        var kyc = client.kyc().createEntityKyc(
                entity.getId(),
                CreateEntityKycRequest.builder()
                        .body(CreateKycInput.baseline(CreateBaselineKycInput.builder()
                                .data(BaselineKycCheckDataV0.builder()
                                        .countryCode("US")
                                        .lastName("Doe")
                                        .addressCountryCode("US")
                                        .firstName("Jane")
                                        .middleName("Marie")
                                        .birthDate("1990-01-01")
                                        .email("[email protected]")
                                        .taxIdNumber("123-45-6789")
                                        .build())
                                .providerName("your-kyc-provider") // Name of the provider that performed the KYC
                                .build()))
                        .build());

        File document = new File("./gov-id.jpeg"); // Replace with your actual document file
        var uploadResponse = client.kyc().createEntityKycDocument(
                entity.getId(),
                kyc.getBaseline().get().getId(),
                document,
                CreateKycDocumentFileInput.builder().documentType(KycDocumentType.GOVERNMENT_ID).build());
        System.out.println(uploadResponse);
    }
}
```

### White-labeled KYC

TypeScriptPythonGoJava

```
import { DinariClient, DinariEnvironment } from "@dinari/api-sdk";

const client = new DinariClient({
  apiKeyId: process.env.DINARI_API_KEY_ID!, // This is the default and can be omitted
  apiSecretKey: process.env.DINARI_API_SECRET_KEY!, // This is the default and can be omitted
  environment: DinariEnvironment.Sandbox, // defaults to DinariEnvironment.Production
});

async function main() {
  const entityId = "0197423b-d4f9-7cdc-80e4-d50814958e44"; // Replace with your actual entity ID

  const kycResponse = await client.kyc.createManagedEntityKycEmbed({ entityId });

  console.log(kycResponse.embedUrl);
}

main();
```

```
import os

from dinari_api_sdk import DinariClient
from dinari_api_sdk.environment import DinariClientEnvironment

client = DinariClient(
    api_key_id=os.environ["DINARI_API_KEY_ID"],  # This is the default and can be omitted
    api_secret_key=os.environ["DINARI_API_SECRET_KEY"],  # This is the default and can be omitted
    environment=DinariClientEnvironment.SANDBOX,  # defaults to DinariClientEnvironment.PRODUCTION
)

entity_id = "0197423b-d4f9-7cdc-80e4-d50814958e44"  # Replace with your actual entity ID

redirect = client.kyc.create_managed_entity_kyc_embed(
    entity_id=entity_id,
)

print("Redirect user to:", redirect.embed_url)
```

```
package main

import (
	"context"
	"fmt"
	"log"
	"os"

	dinari "github.com/dinaricrypto/dinari-api-sdk-go"
	client "github.com/dinaricrypto/dinari-api-sdk-go/client"
	option "github.com/dinaricrypto/dinari-api-sdk-go/option"
)

func main() {
	c := client.NewDinariClient(
		option.WithBaseURL(dinari.Environments.Sandbox), // Defaults to production when omitted
		option.WithAPIKeyID(os.Getenv("DINARI_API_KEY_ID")),
		option.WithAPISecretKey(os.Getenv("DINARI_API_SECRET_KEY")),
	)

	entityID := "0197423b-d4f9-7cdc-80e4-d50814958e44" // Replace with your actual entity ID

	kycResp, err := c.Kyc.CreateManagedEntityKycEmbed(context.Background(), &dinari.CreateManagedKycInput{
		EntityID: entityID,
	})
	if err != nil {
		log.Fatalf("Failed to initiate managed KYC check: %v", err)
	}

	fmt.Printf("KYC Redirect URL: %s\n", kycResp.EmbedURL)
}
```

```
import com.dinari.api.DinariClient;
import com.dinari.api.core.Environment;

public class Main {
    public static void main(String[] args) {
        DinariClient client = DinariClient.builder()
                .environment(Environment.SANDBOX) // defaults to Environment.PRODUCTION
                .apiKeyId(System.getenv("DINARI_API_KEY_ID")) // This is the default and can be omitted
                .apiSecretKey(System.getenv("DINARI_API_SECRET_KEY")) // This is the default and can be omitted
                .build();

        String entityId = "0197423b-d4f9-7cdc-80e4-d50814958e44"; // Replace with your actual entity ID

        var kycResponse = client.kyc().createManagedEntityKycEmbed(entityId);

        System.out.println(kycResponse.getEmbedUrl());
    }
}
```

Updated 6 days ago

---

[Entity Management](https://docs.dinari.com/docs/entity-management)[Managing Accounts](https://docs.dinari.com/docs/managing-accounts)

Did this page help you?

Yes

No

Copy Page

* + [Requirements](https://docs.dinari.com/docs/managing-kyc)
  + - [Integration Types](https://docs.dinari.com/docs/managing-kyc)
    - * [Partner KYC](https://docs.dinari.com/docs/managing-kyc)
      * [Managed KYC](https://docs.dinari.com/docs/managing-kyc)
    - [Supported Identity Verification Providers](https://docs.dinari.com/docs/managing-kyc)
    - [⚠️ Special Jurisdictions](https://docs.dinari.com/docs/managing-kyc)
  + [Integration](https://docs.dinari.com/docs/managing-kyc)
  + - [SDK Reference](https://docs.dinari.com/docs/managing-kyc)
    - [SDK Examples](https://docs.dinari.com/docs/managing-kyc)
    - * [Partner-Managed KYC](https://docs.dinari.com/docs/managing-kyc)
      * [White-labeled KYC](https://docs.dinari.com/docs/managing-kyc)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Identity Verification (KYC)","dateModified":"2026-11-10T17:53:39.000Z"}
```

<<<PAGE https://docs.dinari.com/docs/managing-wallets>>>
---
url: https://docs.dinari.com/docs/managing-wallets
title: Managing Wallets
description: A Wallet represents a wallet on a blockchain. For trading activities to be tracked in Dinari, a wallet must be linked to an Account . The following section provides examples on how to manage wallets on an account. Please note that to manage your organization's wallet, an account id that is linked to…
fetched: 2026-11-16
method: static
plan: read
---

## Getting Started

* [Quickstart](https://docs.dinari.com/docs/quickstart)
* [Deploy to production](https://docs.dinari.com/docs/deploy-to-production)
* [Hosted Trading](https://docs.dinari.com/docs/hosted-trading)

## Core Concepts

* [What are dShares™?](https://docs.dinari.com/docs/what-is-dshare)
  + [Blockchain](https://docs.dinari.com/docs/blockchain)
    - [Wrapping dShares™](https://docs.dinari.com/docs/wrapping)
    - [Hyperliquid](https://docs.dinari.com/docs/hyperliquid)
    - [dShare Bridging Guide](https://docs.dinari.com/docs/dshare-bridging-guide)
    - [Deprecation Notices](https://docs.dinari.com/docs/deprecations)
* [What is USD+?](https://docs.dinari.com/docs/what-is-usd)
  + [Blockchain](https://docs.dinari.com/docs/usdplus-evm)
    - [EVM](https://docs.dinari.com/docs/usdplus-evm)
      * [Integration Guide](https://docs.dinari.com/docs/usdplus-evm-integration-guide)
* [Trading Hours](https://docs.dinari.com/docs/trading-hours)
* [Partner Fees](https://docs.dinari.com/docs/fees)

## Technical Integration

* [Entity Management](https://docs.dinari.com/docs/entity-management)
  + [Identity Verification (KYC)](https://docs.dinari.com/docs/managing-kyc)
  + [Managing Accounts](https://docs.dinari.com/docs/managing-accounts)
  + [Managing Wallets](https://docs.dinari.com/docs/managing-wallets)
  + [Funding Accounts through Wallets](https://docs.dinari.com/docs/funding-accounts-through-wallets)
* [Ordering](https://docs.dinari.com/docs/placing-orders)
  + [Placing Orders](https://docs.dinari.com/docs/placing-orders)
    - [Placing dShare Orders with Alchemy](https://docs.dinari.com/docs/placing-dshare-orders-with-alchemy)
    - [Placing dShare Orders with Safe Vaults](https://docs.dinari.com/docs/placing-dshare-orders-with-safe-vaults)
  + [Order Types & Behaviors](https://docs.dinari.com/docs/order-type)
  + [Order Fulfillment Amounts in the Orders API](https://docs.dinari.com/docs/order-fulfillment-amounts-in-the-orders-api)
* [Stock Data](https://docs.dinari.com/docs/stock-data)
  + [Pricing & Quotes](https://docs.dinari.com/docs/pricing-quotes)
  + [24/7 Tradable Assets](https://docs.dinari.com/docs/24-7-trading)
  + [24/5 Tradable Assets](https://docs.dinari.com/docs/245-tradable-assets)
* [Corporate Actions](https://docs.dinari.com/docs/corporate-action-processing)
  + [Dividends](https://docs.dinari.com/docs/dividend-payments)
  + [Stock Splits](https://docs.dinari.com/docs/stock-split-handling)
  + [Ticker Changes](https://docs.dinari.com/docs/ticker-changes)
  + [Mergers](https://docs.dinari.com/docs/mergers)
* [Websockets for Order Data (BETA)](https://docs.dinari.com/docs/websockets)
* [Troubleshooting & Known Issues](https://docs.dinari.com/docs/error-codes)
  + [Error Codes](https://docs.dinari.com/docs/error-codes)
  + [Orders Stuck in SUBMITTED Status](https://docs.dinari.com/docs/stuck-orders)
  + [Smart Contract Wallet Support](https://docs.dinari.com/docs/smart-contract-wallet-support)

## Compliance and Regional

* [Security](https://docs.dinari.com/docs/security)
* [Regional Requirements](https://docs.dinari.com/docs/regional-requirements)
  + [US Customers](https://docs.dinari.com/docs/us)
* [Restrictions](https://docs.dinari.com/docs/restrictions)
* [Taxes & Reporting](https://docs.dinari.com/docs/taxes-reporting)

## Support

* [Staying Safe on Dinari](https://docs.dinari.com/docs/staying-safe-on-dinari)
* [FAQs](https://docs.dinari.com/docs/faqs)
* [Status Pages](https://docs.dinari.com/docs/status-pages)

Powered by

# Managing Wallets

A `Wallet` represents a wallet on a blockchain. For trading activities to be tracked in Dinari, a wallet must be linked to an `Account`. The following section provides examples on how to manage wallets on an account. Please note that to manage your organization's wallet, an account id that is linked to the entity id provided in your dashboard must be used.

# Dinari-managed Wallets

> ❗️
>
> ### This will only work on your organization's accounts

To create a Dinari-managed wallet, visit your dashboard and do the following:

1. Click on `Create Account`

2. On the row for the new Account created, click on `+ Connect Wallet`

  

3. A modal will pop up. Select `Use a Managed Wallet` and click `Submit`

# External Wallets

## SDK Reference

| Language | URL |
| --- | --- |
| Javascript / Typescript | [https://github.com/dinaricrypto/dinari-api-sdk-typescript/blob/main/reference.md#wallets](https://github.com/dinaricrypto/dinari-api-sdk-typescript/blob/main/reference.md) |
| Python | [https://github.com/dinaricrypto/dinari-api-sdk-python/blob/main/reference.md#wallets](https://github.com/dinaricrypto/dinari-api-sdk-python/blob/main/reference.md) |
| Go | [https://github.com/dinaricrypto/dinari-api-sdk-go/blob/main/reference.md#wallets](https://github.com/dinaricrypto/dinari-api-sdk-go/blob/main/reference.md) |
| Java | [https://github.com/dinaricrypto/dinari-api-sdk-java/blob/main/reference.md#wallets](https://github.com/dinaricrypto/dinari-api-sdk-java/blob/main/reference.md) |

## SDK Examples

## Connecting a Wallet to an Account

TypeScriptPythonGoJava

```
import { DinariClient, DinariEnvironment } from "@dinari/api-sdk";

const client = new DinariClient({
  apiKeyId: process.env.DINARI_API_KEY_ID!, // This is the default and can be omitted
  apiSecretKey: process.env.DINARI_API_SECRET_KEY!, // This is the default and can be omitted
  environment: DinariEnvironment.Sandbox, // defaults to DinariEnvironment.Production
});

async function main() {
  const accountId = "your-account-id";
  const walletAddress = "your-wallet-address";

  // Step 1: Get the nonce message to sign
  const nonceResp = await client.wallets.getAccountWalletConnectionNonce({
    accountId,
    walletAddress,
    chainId: "eip155:1",
  });

  // Step 2: Sign the message (replace this with actual off-chain signing)
  const signature = "your-wallet-signature"; // Sign nonceResp.message with the wallet

  // Step 3: Connect the wallet using the signed message
  const linkedWallet = await client.wallets.createAccountWalletConnection({
    accountId,
    chainId: "eip155:1",
    nonce: nonceResp.nonce,
    signature,
    walletAddress,
  });

  console.log(linkedWallet);
}

main();
```

```
import os

from dinari_api_sdk import DinariClient
from dinari_api_sdk.environment import DinariClientEnvironment

client = DinariClient(
    api_key_id=os.environ["DINARI_API_KEY_ID"],  # This is the default and can be omitted
    api_secret_key=os.environ["DINARI_API_SECRET_KEY"],  # This is the default and can be omitted
    environment=DinariClientEnvironment.SANDBOX,  # defaults to DinariClientEnvironment.PRODUCTION
)

account_id = "your-account-id"
wallet_address = "your-wallet-address"

# Step 1: Get the nonce message to sign
nonce_resp = client.wallets.get_account_wallet_connection_nonce(
    account_id=account_id,
    wallet_address=wallet_address,
    chain_id="eip155:1",
)

# Step 2: Sign the message (replace this with actual off-chain signing)
signature = "your-wallet-signature"  # Sign nonce_resp.message with the wallet

# Step 3: Connect the wallet using the signed message
linked_wallet = client.wallets.create_account_wallet_connection(
    account_id=account_id,
    chain_id="eip155:1",
    nonce=nonce_resp.nonce,
    signature=signature,
    wallet_address=wallet_address,
)
print(linked_wallet)
```

```
package main

import (
	"context"
	"fmt"
	"log"
	"os"

	dinari "github.com/dinaricrypto/dinari-api-sdk-go"
	client "github.com/dinaricrypto/dinari-api-sdk-go/client"
	option "github.com/dinaricrypto/dinari-api-sdk-go/option"
)

func main() {
	c := client.NewDinariClient(
		option.WithBaseURL(dinari.Environments.Sandbox), // Defaults to production when omitted
		option.WithAPIKeyID(os.Getenv("DINARI_API_KEY_ID")),
		option.WithAPISecretKey(os.Getenv("DINARI_API_SECRET_KEY")),
	)

	accountID := "your-account-id"
	walletAddress := "your-wallet-address"

	// Step 1: Get the nonce message to sign
	nonceResp, err := c.Wallets.GetAccountWalletConnectionNonce(context.Background(), &dinari.GetAccountWalletConnectionNonceRequest{
		AccountID:     accountID,
		WalletAddress: walletAddress,
		ChainID:       dinari.WalletChainIDEip1551,
	})
	if err != nil {
		log.Fatalf("Failed to get wallet nonce: %v", err)
	}

	// Step 2: Sign the message (replace this with actual off-chain signing)
	signature := "your-wallet-signature" // Sign nonceResp.Message with the wallet

	// Step 3: Connect the wallet using the signed message
	linkedWallet, err := c.Wallets.CreateAccountWalletConnection(context.Background(), &dinari.CreateAccountWalletConnectionInput{
		AccountID:     accountID,
		ChainID:       dinari.WalletChainIDEip1551,
		Nonce:         nonceResp.Nonce,
		Signature:     signature,
		WalletAddress: walletAddress,
	})
	if err != nil {
		log.Fatalf("Failed to connect external wallet: %v", err)
	}

	fmt.Printf("Linked Wallet: %+v\n", linkedWallet)
}
```

```
import com.dinari.api.DinariClient;
import com.dinari.api.core.Environment;
import com.dinari.api.resources.wallets.requests.CreateAccountWalletConnectionInput;
import com.dinari.api.resources.wallets.requests.GetAccountWalletConnectionNonceRequest;
import com.dinari.api.types.WalletChainId;

public class Main {
    public static void main(String[] args) {
        DinariClient client = DinariClient.builder()
                .environment(Environment.SANDBOX) // defaults to Environment.PRODUCTION
                .apiKeyId(System.getenv("DINARI_API_KEY_ID")) // This is the default and can be omitted
                .apiSecretKey(System.getenv("DINARI_API_SECRET_KEY")) // This is the default and can be omitted
                .build();

        String accountId = "your-account-id";
        String walletAddress = "your-wallet-address";

        // Step 1: Get the nonce message to sign
        var nonceResp = client.wallets().getAccountWalletConnectionNonce(
                accountId,
                GetAccountWalletConnectionNonceRequest.builder()
                        .walletAddress(walletAddress)
                        .chainId(WalletChainId.EIP1551)
                        .build());

        // Step 2: Sign the message (replace this with actual off-chain signing)
        String signature = "your-wallet-signature"; // Sign nonceResp.getMessage() with the wallet

        // Step 3: Connect the wallet using the signed message
        var linkedWallet = client.wallets().createAccountWalletConnection(
                accountId,
                CreateAccountWalletConnectionInput.builder()
                        .signature(signature)
                        .nonce(nonceResp.getNonce())
                        .walletAddress(walletAddress)
                        .chainId(WalletChainId.EIP1551)
                        .build());
        System.out.println(linkedWallet);
    }
}
```

Updated 6 days ago

---

[Managing Accounts](https://docs.dinari.com/docs/managing-accounts)[Funding Accounts through Wallets](https://docs.dinari.com/docs/funding-accounts-through-wallets)

Did this page help you?

Yes

No

Copy Page

* + [Dinari-managed Wallets](https://docs.dinari.com/docs/managing-wallets)
  + [External Wallets](https://docs.dinari.com/docs/managing-wallets)
  + - [SDK Reference](https://docs.dinari.com/docs/managing-wallets)
    - [SDK Examples](https://docs.dinari.com/docs/managing-wallets)
    - [Connecting a Wallet to an Account](https://docs.dinari.com/docs/managing-wallets)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Managing Wallets","dateModified":"2026-11-10T17:53:39.000Z"}
```

<<<PAGE https://docs.dinari.com/docs/24-7-trading>>>
---
url: https://docs.dinari.com/docs/24-7-trading
title: 24/7 Tradable Assets
description: The dShares™ currently eligible for trading during the Open (24/7) session.
fetched: 2026-11-16
method: static
plan: read
---

## Getting Started

* [Quickstart](https://docs.dinari.com/docs/quickstart)
* [Deploy to production](https://docs.dinari.com/docs/deploy-to-production)
* [Hosted Trading](https://docs.dinari.com/docs/hosted-trading)

## Core Concepts

* [What are dShares™?](https://docs.dinari.com/docs/what-is-dshare)
  + [Blockchain](https://docs.dinari.com/docs/blockchain)
    - [Wrapping dShares™](https://docs.dinari.com/docs/wrapping)
    - [Hyperliquid](https://docs.dinari.com/docs/hyperliquid)
    - [dShare Bridging Guide](https://docs.dinari.com/docs/dshare-bridging-guide)
    - [Deprecation Notices](https://docs.dinari.com/docs/deprecations)
* [What is USD+?](https://docs.dinari.com/docs/what-is-usd)
  + [Blockchain](https://docs.dinari.com/docs/usdplus-evm)
    - [EVM](https://docs.dinari.com/docs/usdplus-evm)
      * [Integration Guide](https://docs.dinari.com/docs/usdplus-evm-integration-guide)
* [Trading Hours](https://docs.dinari.com/docs/trading-hours)
* [Partner Fees](https://docs.dinari.com/docs/fees)

## Technical Integration

* [Entity Management](https://docs.dinari.com/docs/entity-management)
  + [Identity Verification (KYC)](https://docs.dinari.com/docs/managing-kyc)
  + [Managing Accounts](https://docs.dinari.com/docs/managing-accounts)
  + [Managing Wallets](https://docs.dinari.com/docs/managing-wallets)
  + [Funding Accounts through Wallets](https://docs.dinari.com/docs/funding-accounts-through-wallets)
* [Ordering](https://docs.dinari.com/docs/placing-orders)
  + [Placing Orders](https://docs.dinari.com/docs/placing-orders)
    - [Placing dShare Orders with Alchemy](https://docs.dinari.com/docs/placing-dshare-orders-with-alchemy)
    - [Placing dShare Orders with Safe Vaults](https://docs.dinari.com/docs/placing-dshare-orders-with-safe-vaults)
  + [Order Types & Behaviors](https://docs.dinari.com/docs/order-type)
  + [Order Fulfillment Amounts in the Orders API](https://docs.dinari.com/docs/order-fulfillment-amounts-in-the-orders-api)
* [Stock Data](https://docs.dinari.com/docs/stock-data)
  + [Pricing & Quotes](https://docs.dinari.com/docs/pricing-quotes)
  + [24/7 Tradable Assets](https://docs.dinari.com/docs/24-7-trading)
  + [24/5 Tradable Assets](https://docs.dinari.com/docs/245-tradable-assets)
* [Corporate Actions](https://docs.dinari.com/docs/corporate-action-processing)
  + [Dividends](https://docs.dinari.com/docs/dividend-payments)
  + [Stock Splits](https://docs.dinari.com/docs/stock-split-handling)
  + [Ticker Changes](https://docs.dinari.com/docs/ticker-changes)
  + [Mergers](https://docs.dinari.com/docs/mergers)
* [Websockets for Order Data (BETA)](https://docs.dinari.com/docs/websockets)
* [Troubleshooting & Known Issues](https://docs.dinari.com/docs/error-codes)
  + [Error Codes](https://docs.dinari.com/docs/error-codes)
  + [Orders Stuck in SUBMITTED Status](https://docs.dinari.com/docs/stuck-orders)
  + [Smart Contract Wallet Support](https://docs.dinari.com/docs/smart-contract-wallet-support)

## Compliance and Regional

* [Security](https://docs.dinari.com/docs/security)
* [Regional Requirements](https://docs.dinari.com/docs/regional-requirements)
  + [US Customers](https://docs.dinari.com/docs/us)
* [Restrictions](https://docs.dinari.com/docs/restrictions)
* [Taxes & Reporting](https://docs.dinari.com/docs/taxes-reporting)

## Support

* [Staying Safe on Dinari](https://docs.dinari.com/docs/staying-safe-on-dinari)
* [FAQs](https://docs.dinari.com/docs/faqs)
* [Status Pages](https://docs.dinari.com/docs/status-pages)

Powered by

# 24/7 Tradable Assets

The dShares™ currently eligible for trading during the Open (24/7) session.

Dinari supports 24/7 order placement for a specific subset of the dShares™ catalog, allowing orders to be submitted and processed even when standard U.S. markets are closed. All other dShare's in the catalog remains tradable during the Regular, Extended, and Overnight sessions as normal.

| Ticker | Asset Name | Type |
| --- | --- | --- |
| SPY | SPDR® S&P 500® ETF Trust | ETF |
| QQQ | Invesco QQQ Trust℠ | ETF |
| AAPL | Apple Inc. | Stock |
| AMZN | Amazon.com, Inc. | Stock |
| META | Meta Platforms, Inc. | Stock |
| MSTR | Strategy Inc. | Stock |
| NVDA | NVIDIA Corporation | Stock |
| SPCX | Space Exploration Technologies Corp. (SpaceX) | Stock |
| TSLA | Tesla, Inc. | Stock |

> ***Please Note: This list is occasionally updating and will continue to grow as more assets become available for 24/7 trading.***

Updated about 1 month ago

---

[Pricing & Quotes](https://docs.dinari.com/docs/pricing-quotes)[24/5 Tradable Assets](https://docs.dinari.com/docs/245-tradable-assets)

Did this page help you?

Yes

No

Copy Page

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"24/7 Tradable Assets","dateModified":"2026-10-14T11:29:03.000Z"}
```

<<<PAGE https://docs.dinari.com/docs/245-tradable-assets>>>
---
url: https://docs.dinari.com/docs/245-tradable-assets
title: 24/5 Tradable Assets
description: The dShares™ currently eligible for trading during the Regular, Extended, and Overnight (24/5) sessions.
fetched: 2026-11-16
method: static
plan: read
---

## Getting Started

* [Quickstart](https://docs.dinari.com/docs/quickstart)
* [Deploy to production](https://docs.dinari.com/docs/deploy-to-production)
* [Hosted Trading](https://docs.dinari.com/docs/hosted-trading)

## Core Concepts

* [What are dShares™?](https://docs.dinari.com/docs/what-is-dshare)
  + [Blockchain](https://docs.dinari.com/docs/blockchain)
    - [Wrapping dShares™](https://docs.dinari.com/docs/wrapping)
    - [Hyperliquid](https://docs.dinari.com/docs/hyperliquid)
    - [dShare Bridging Guide](https://docs.dinari.com/docs/dshare-bridging-guide)
    - [Deprecation Notices](https://docs.dinari.com/docs/deprecations)
* [What is USD+?](https://docs.dinari.com/docs/what-is-usd)
  + [Blockchain](https://docs.dinari.com/docs/usdplus-evm)
    - [EVM](https://docs.dinari.com/docs/usdplus-evm)
      * [Integration Guide](https://docs.dinari.com/docs/usdplus-evm-integration-guide)
* [Trading Hours](https://docs.dinari.com/docs/trading-hours)
* [Partner Fees](https://docs.dinari.com/docs/fees)

## Technical Integration

* [Entity Management](https://docs.dinari.com/docs/entity-management)
  + [Identity Verification (KYC)](https://docs.dinari.com/docs/managing-kyc)
  + [Managing Accounts](https://docs.dinari.com/docs/managing-accounts)
  + [Managing Wallets](https://docs.dinari.com/docs/managing-wallets)
  + [Funding Accounts through Wallets](https://docs.dinari.com/docs/funding-accounts-through-wallets)
* [Ordering](https://docs.dinari.com/docs/placing-orders)
  + [Placing Orders](https://docs.dinari.com/docs/placing-orders)
    - [Placing dShare Orders with Alchemy](https://docs.dinari.com/docs/placing-dshare-orders-with-alchemy)
    - [Placing dShare Orders with Safe Vaults](https://docs.dinari.com/docs/placing-dshare-orders-with-safe-vaults)
  + [Order Types & Behaviors](https://docs.dinari.com/docs/order-type)
  + [Order Fulfillment Amounts in the Orders API](https://docs.dinari.com/docs/order-fulfillment-amounts-in-the-orders-api)
* [Stock Data](https://docs.dinari.com/docs/stock-data)
  + [Pricing & Quotes](https://docs.dinari.com/docs/pricing-quotes)
  + [24/7 Tradable Assets](https://docs.dinari.com/docs/24-7-trading)
  + [24/5 Tradable Assets](https://docs.dinari.com/docs/245-tradable-assets)
* [Corporate Actions](https://docs.dinari.com/docs/corporate-action-processing)
  + [Dividends](https://docs.dinari.com/docs/dividend-payments)
  + [Stock Splits](https://docs.dinari.com/docs/stock-split-handling)
  + [Ticker Changes](https://docs.dinari.com/docs/ticker-changes)
  + [Mergers](https://docs.dinari.com/docs/mergers)
* [Websockets for Order Data (BETA)](https://docs.dinari.com/docs/websockets)
* [Troubleshooting & Known Issues](https://docs.dinari.com/docs/error-codes)
  + [Error Codes](https://docs.dinari.com/docs/error-codes)
  + [Orders Stuck in SUBMITTED Status](https://docs.dinari.com/docs/stuck-orders)
  + [Smart Contract Wallet Support](https://docs.dinari.com/docs/smart-contract-wallet-support)

## Compliance and Regional

* [Security](https://docs.dinari.com/docs/security)
* [Regional Requirements](https://docs.dinari.com/docs/regional-requirements)
  + [US Customers](https://docs.dinari.com/docs/us)
* [Restrictions](https://docs.dinari.com/docs/restrictions)
* [Taxes & Reporting](https://docs.dinari.com/docs/taxes-reporting)

## Support

* [Staying Safe on Dinari](https://docs.dinari.com/docs/staying-safe-on-dinari)
* [FAQs](https://docs.dinari.com/docs/faqs)
* [Status Pages](https://docs.dinari.com/docs/status-pages)

Powered by

# 24/5 Tradable Assets

The dShares™ currently eligible for trading during the Regular, Extended, and Overnight (24/5) sessions.

Copy Page

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"24/5 Tradable Assets","dateModified":"2026-10-14T11:29:03.000Z"}
```

<<<PAGE https://docs.dinari.com/docs/stock-data>>>
---
url: https://docs.dinari.com/docs/stock-data
title: Stock Data
description: This section provides examples on retrieving the list of stocks supported on Dinari and supporting metadata for those stocks. SDK References Language URL Javascript / Typescript https://github.com/dinaricrypto/dinari-api-sdk-typescript/blob/main/reference.md#market-data Python https://github.com/din…
fetched: 2026-11-16
method: static
plan: read
---

## Getting Started

* [Quickstart](https://docs.dinari.com/docs/quickstart)
* [Deploy to production](https://docs.dinari.com/docs/deploy-to-production)
* [Hosted Trading](https://docs.dinari.com/docs/hosted-trading)

## Core Concepts

* [What are dShares™?](https://docs.dinari.com/docs/what-is-dshare)
  + [Blockchain](https://docs.dinari.com/docs/blockchain)
    - [Wrapping dShares™](https://docs.dinari.com/docs/wrapping)
    - [Hyperliquid](https://docs.dinari.com/docs/hyperliquid)
    - [dShare Bridging Guide](https://docs.dinari.com/docs/dshare-bridging-guide)
    - [Deprecation Notices](https://docs.dinari.com/docs/deprecations)
* [What is USD+?](https://docs.dinari.com/docs/what-is-usd)
  + [Blockchain](https://docs.dinari.com/docs/usdplus-evm)
    - [EVM](https://docs.dinari.com/docs/usdplus-evm)
      * [Integration Guide](https://docs.dinari.com/docs/usdplus-evm-integration-guide)
* [Trading Hours](https://docs.dinari.com/docs/trading-hours)
* [Partner Fees](https://docs.dinari.com/docs/fees)

## Technical Integration

* [Entity Management](https://docs.dinari.com/docs/entity-management)
  + [Identity Verification (KYC)](https://docs.dinari.com/docs/managing-kyc)
  + [Managing Accounts](https://docs.dinari.com/docs/managing-accounts)
  + [Managing Wallets](https://docs.dinari.com/docs/managing-wallets)
  + [Funding Accounts through Wallets](https://docs.dinari.com/docs/funding-accounts-through-wallets)
* [Ordering](https://docs.dinari.com/docs/placing-orders)
  + [Placing Orders](https://docs.dinari.com/docs/placing-orders)
    - [Placing dShare Orders with Alchemy](https://docs.dinari.com/docs/placing-dshare-orders-with-alchemy)
    - [Placing dShare Orders with Safe Vaults](https://docs.dinari.com/docs/placing-dshare-orders-with-safe-vaults)
  + [Order Types & Behaviors](https://docs.dinari.com/docs/order-type)
  + [Order Fulfillment Amounts in the Orders API](https://docs.dinari.com/docs/order-fulfillment-amounts-in-the-orders-api)
* [Stock Data](https://docs.dinari.com/docs/stock-data)
  + [Pricing & Quotes](https://docs.dinari.com/docs/pricing-quotes)
  + [24/7 Tradable Assets](https://docs.dinari.com/docs/24-7-trading)
  + [24/5 Tradable Assets](https://docs.dinari.com/docs/245-tradable-assets)
* [Corporate Actions](https://docs.dinari.com/docs/corporate-action-processing)
  + [Dividends](https://docs.dinari.com/docs/dividend-payments)
  + [Stock Splits](https://docs.dinari.com/docs/stock-split-handling)
  + [Ticker Changes](https://docs.dinari.com/docs/ticker-changes)
  + [Mergers](https://docs.dinari.com/docs/mergers)
* [Websockets for Order Data (BETA)](https://docs.dinari.com/docs/websockets)
* [Troubleshooting & Known Issues](https://docs.dinari.com/docs/error-codes)
  + [Error Codes](https://docs.dinari.com/docs/error-codes)
  + [Orders Stuck in SUBMITTED Status](https://docs.dinari.com/docs/stuck-orders)
  + [Smart Contract Wallet Support](https://docs.dinari.com/docs/smart-contract-wallet-support)

## Compliance and Regional

* [Security](https://docs.dinari.com/docs/security)
* [Regional Requirements](https://docs.dinari.com/docs/regional-requirements)
  + [US Customers](https://docs.dinari.com/docs/us)
* [Restrictions](https://docs.dinari.com/docs/restrictions)
* [Taxes & Reporting](https://docs.dinari.com/docs/taxes-reporting)

## Support

* [Staying Safe on Dinari](https://docs.dinari.com/docs/staying-safe-on-dinari)
* [FAQs](https://docs.dinari.com/docs/faqs)
* [Status Pages](https://docs.dinari.com/docs/status-pages)

Powered by

# Stock Data

This section provides examples on retrieving the list of stocks supported on Dinari and supporting metadata for those stocks.

# SDK References

| Language | URL |
| --- | --- |
| Javascript / Typescript | [https://github.com/dinaricrypto/dinari-api-sdk-typescript/blob/main/reference.md#market-data](https://github.com/dinaricrypto/dinari-api-sdk-typescript/blob/main/reference.md) |
| Python | [https://github.com/dinaricrypto/dinari-api-sdk-python/blob/main/reference.md#market-data](https://github.com/dinaricrypto/dinari-api-sdk-python/blob/main/reference.md) |
| Go | [https://github.com/dinaricrypto/dinari-api-sdk-go/blob/main/reference.md#market-data](https://github.com/dinaricrypto/dinari-api-sdk-go/blob/main/reference.md) |
| Java | [https://github.com/dinaricrypto/dinari-api-sdk-java/blob/main/reference.md#market-data](https://github.com/dinaricrypto/dinari-api-sdk-java/blob/main/reference.md) |

# SDK Examples

## Get list of Stocks

TypeScriptPythonGoJava

```
import { DinariClient, DinariEnvironment } from "@dinari/api-sdk";

const client = new DinariClient({
  apiKeyId: process.env.DINARI_API_KEY_ID!, // This is the default and can be omitted
  apiSecretKey: process.env.DINARI_API_SECRET_KEY!, // This is the default and can be omitted
  environment: DinariEnvironment.Sandbox, // defaults to DinariEnvironment.Production
});

async function main() {
  const stocks = await client.marketData.getStocks({ limit: 20 });
  console.log(stocks);
}

main();
```

```
import os

from dinari_api_sdk import DinariClient
from dinari_api_sdk.environment import DinariClientEnvironment

client = DinariClient(
    api_key_id=os.environ["DINARI_API_KEY_ID"],  # This is the default and can be omitted
    api_secret_key=os.environ["DINARI_API_SECRET_KEY"],  # This is the default and can be omitted
    environment=DinariClientEnvironment.SANDBOX,  # defaults to DinariClientEnvironment.PRODUCTION
)

stocks = client.market_data.get_stocks(limit=20)
print(stocks)
```

```
package main

import (
	"context"
	"fmt"
	"log"
	"os"

	dinari "github.com/dinaricrypto/dinari-api-sdk-go"
	client "github.com/dinaricrypto/dinari-api-sdk-go/client"
	option "github.com/dinaricrypto/dinari-api-sdk-go/option"
)

func main() {
	c := client.NewDinariClient(
		option.WithBaseURL(dinari.Environments.Sandbox), // Defaults to production when omitted
		option.WithAPIKeyID(os.Getenv("DINARI_API_KEY_ID")),
		option.WithAPISecretKey(os.Getenv("DINARI_API_SECRET_KEY")),
	)

	// Example: Get a list of all stocks
	stocks, err := c.MarketData.GetStocks(context.Background(), &dinari.GetStocksRequest{
		Limit: dinari.Int(20),
	})
	if err != nil {
		log.Fatalf("Failed to list stocks: %v", err)
	}

	fmt.Printf("Stocks: %+v\n", stocks)
}
```

```
import com.dinari.api.DinariClient;
import com.dinari.api.core.Environment;
import com.dinari.api.resources.marketdata.requests.GetStocksRequest;

public class Main {
    public static void main(String[] args) {
        DinariClient client = DinariClient.builder()
                .environment(Environment.SANDBOX) // defaults to Environment.PRODUCTION
                .apiKeyId(System.getenv("DINARI_API_KEY_ID")) // This is the default and can be omitted
                .apiSecretKey(System.getenv("DINARI_API_SECRET_KEY")) // This is the default and can be omitted
                .build();

        var stocks = client.marketData().getStocks(GetStocksRequest.builder().limit(20).build());
        System.out.println(stocks);
    }
}
```

## Get historical prices for a Stock

TypeScriptPythonGoJava

```
import { DinariClient, DinariEnvironment } from "@dinari/api-sdk";

const client = new DinariClient({
  apiKeyId: process.env.DINARI_API_KEY_ID!, // This is the default and can be omitted
  apiSecretKey: process.env.DINARI_API_SECRET_KEY!, // This is the default and can be omitted
  environment: DinariEnvironment.Sandbox, // defaults to DinariEnvironment.Production
});

async function main() {
  const stockId = "stock-id-here"; // Replace with the actual Stock ID

  const prices = await client.marketData.getStockPriceChart({
    stockId,
    timespan: "DAY",
  });

  console.log(prices);
}

main();
```

```
import os

from dinari_api_sdk import DinariClient
from dinari_api_sdk.environment import DinariClientEnvironment

client = DinariClient(
    api_key_id=os.environ["DINARI_API_KEY_ID"],  # This is the default and can be omitted
    api_secret_key=os.environ["DINARI_API_SECRET_KEY"],  # This is the default and can be omitted
    environment=DinariClientEnvironment.SANDBOX,  # defaults to DinariClientEnvironment.PRODUCTION
)

prices = client.market_data.get_stock_price_chart(
    stock_id="stock-id-here",  # Replace with the actual Stock ID
    timespan="DAY",
)
print(prices)
```

```
package main

import (
	"context"
	"fmt"
	"log"
	"os"

	dinari "github.com/dinaricrypto/dinari-api-sdk-go"
	client "github.com/dinaricrypto/dinari-api-sdk-go/client"
	option "github.com/dinaricrypto/dinari-api-sdk-go/option"
)

func main() {
	c := client.NewDinariClient(
		option.WithBaseURL(dinari.Environments.Sandbox), // Defaults to production when omitted
		option.WithAPIKeyID(os.Getenv("DINARI_API_KEY_ID")),
		option.WithAPISecretKey(os.Getenv("DINARI_API_SECRET_KEY")),
	)

	stockID := "target-stock-uuid" // Replace with the actual Stock ID

	prices, err := c.MarketData.GetStockPriceChart(context.Background(), &dinari.GetStockPriceChartRequest{
		StockID:  stockID,
		Timespan: dinari.StockTickTimespan1Day,
	})
	if err != nil {
		log.Fatalf("Error getting historical prices: %v", err)
	}

	fmt.Printf("Response: %+v\n", prices)
}
```

```
import com.dinari.api.DinariClient;
import com.dinari.api.core.Environment;
import com.dinari.api.resources.marketdata.requests.GetStockPriceChartRequest;
import com.dinari.api.types.StockTickTimespan1;

public class Main {
    public static void main(String[] args) {
        DinariClient client = DinariClient.builder()
                .environment(Environment.SANDBOX) // defaults to Environment.PRODUCTION
                .apiKeyId(System.getenv("DINARI_API_KEY_ID")) // This is the default and can be omitted
                .apiSecretKey(System.getenv("DINARI_API_SECRET_KEY")) // This is the default and can be omitted
                .build();

        String stockId = "stock-id-here"; // Replace with the actual Stock ID

        var prices = client.marketData().getStockPriceChart(
                stockId,
                GetStockPriceChartRequest.builder().timespan(StockTickTimespan1.DAY).build());
        System.out.println(prices);
    }
}
```

## Get news for a Stock

TypeScriptPythonGoJava

```
import { DinariClient, DinariEnvironment } from "@dinari/api-sdk";

const client = new DinariClient({
  apiKeyId: process.env.DINARI_API_KEY_ID!, // This is the default and can be omitted
  apiSecretKey: process.env.DINARI_API_SECRET_KEY!, // This is the default and can be omitted
  environment: DinariEnvironment.Sandbox, // defaults to DinariEnvironment.Production
});

async function main() {
  const stockId = "stock-id-here"; // Replace with the actual Stock ID

  // Optionally specify a limit on the number of news articles returned
  const news = await client.marketData.getStockNewsByStockId({ stockId, limit: 5 });

  console.log(news);
}

main();
```

```
import os

from dinari_api_sdk import DinariClient
from dinari_api_sdk.environment import DinariClientEnvironment

client = DinariClient(
    api_key_id=os.environ["DINARI_API_KEY_ID"],  # This is the default and can be omitted
    api_secret_key=os.environ["DINARI_API_SECRET_KEY"],  # This is the default and can be omitted
    environment=DinariClientEnvironment.SANDBOX,  # defaults to DinariClientEnvironment.PRODUCTION
)

news = client.market_data.get_stock_news_by_stock_id(
    stock_id="stock-id-here",  # Replace with the actual Stock ID
    limit=5,
)
print(news)
```

```
package main

import (
	"context"
	"fmt"
	"log"
	"os"

	dinari "github.com/dinaricrypto/dinari-api-sdk-go"
	client "github.com/dinaricrypto/dinari-api-sdk-go/client"
	option "github.com/dinaricrypto/dinari-api-sdk-go/option"
)

func main() {
	c := client.NewDinariClient(
		option.WithBaseURL(dinari.Environments.Sandbox), // Defaults to production when omitted
		option.WithAPIKeyID(os.Getenv("DINARI_API_KEY_ID")),
		option.WithAPISecretKey(os.Getenv("DINARI_API_SECRET_KEY")),
	)

	stockID := "target-stock-uuid" // Replace with the actual Stock ID

	news, err := c.MarketData.GetStockNewsByStockID(context.Background(), &dinari.GetStockNewsByStockIDRequest{
		StockID: stockID,
		Limit:   dinari.Int(5),
	})
	if err != nil {
		log.Fatalf("Failed to get stock news: %v", err)
	}

	fmt.Printf("News: %+v\n", news)
}
```

```
import com.dinari.api.DinariClient;
import com.dinari.api.core.Environment;
import com.dinari.api.resources.marketdata.requests.GetStockNewsByStockIdRequest;

public class Main {
    public static void main(String[] args) {
        DinariClient client = DinariClient.builder()
                .environment(Environment.SANDBOX) // defaults to Environment.PRODUCTION
                .apiKeyId(System.getenv("DINARI_API_KEY_ID")) // This is the default and can be omitted
                .apiSecretKey(System.getenv("DINARI_API_SECRET_KEY")) // This is the default and can be omitted
                .build();

        String stockId = "stock-id-here"; // Replace with the actual Stock ID

        // Optionally specify a limit on the number of news articles returned
        var news = client.marketData().getStockNewsByStockId(
                stockId,
                GetStockNewsByStockIdRequest.builder().limit(5).build());
        System.out.println(news);
    }
}
```

## Get live market quote for a Stock

TypeScriptPythonGoJava

```
import { DinariClient, DinariEnvironment } from "@dinari/api-sdk";

const client = new DinariClient({
  apiKeyId: process.env.DINARI_API_KEY_ID!, // This is the default and can be omitted
  apiSecretKey: process.env.DINARI_API_SECRET_KEY!, // This is the default and can be omitted
  environment: DinariEnvironment.Sandbox, // defaults to DinariEnvironment.Production
});

async function main() {
  const stockId = "stock-id-here"; // Replace with the actual Stock ID

  const quote = await client.marketData.getStockCurrentQuotesRouteV2({ stockId });

  console.log(quote);
}

main();
```

```
import os

from dinari_api_sdk import DinariClient
from dinari_api_sdk.environment import DinariClientEnvironment

client = DinariClient(
    api_key_id=os.environ["DINARI_API_KEY_ID"],  # This is the default and can be omitted
    api_secret_key=os.environ["DINARI_API_SECRET_KEY"],  # This is the default and can be omitted
    environment=DinariClientEnvironment.SANDBOX,  # defaults to DinariClientEnvironment.PRODUCTION
)

quote = client.market_data.get_stock_current_quotes_route_v2(
    stock_id="stock-id-here",  # Replace with the actual Stock ID
)
print(quote)
```

```
package main

import (
	"context"
	"fmt"
	"log"
	"os"

	dinari "github.com/dinaricrypto/dinari-api-sdk-go"
	client "github.com/dinaricrypto/dinari-api-sdk-go/client"
	option "github.com/dinaricrypto/dinari-api-sdk-go/option"
)

func main() {
	c := client.NewDinariClient(
		option.WithBaseURL(dinari.Environments.Sandbox), // Defaults to production when omitted
		option.WithAPIKeyID(os.Getenv("DINARI_API_KEY_ID")),
		option.WithAPISecretKey(os.Getenv("DINARI_API_SECRET_KEY")),
	)

	stockID := "target-stock-uuid" // Replace with the actual Stock ID

	quote, err := c.MarketData.GetStockCurrentQuotesRouteV2(context.Background(), &dinari.GetStockCurrentQuotesRouteV2Request{
		StockID: stockID,
	})
	if err != nil {
		log.Fatalf("Failed to get stock quote: %v", err)
	}

	fmt.Printf("Quote: %+v\n", quote)
}
```

```
import com.dinari.api.DinariClient;
import com.dinari.api.core.Environment;

public class Main {
    public static void main(String[] args) {
        DinariClient client = DinariClient.builder()
                .environment(Environment.SANDBOX) // defaults to Environment.PRODUCTION
                .apiKeyId(System.getenv("DINARI_API_KEY_ID")) // This is the default and can be omitted
                .apiSecretKey(System.getenv("DINARI_API_SECRET_KEY")) // This is the default and can be omitted
                .build();

        String stockId = "stock-id-here"; // Replace with the actual Stock ID

        var quote = client.marketData().getStockCurrentQuotesRouteV2(stockId);
        System.out.println(quote);
    }
}
```

Updated 6 days ago

---

[Order Fulfillment Amounts in the Orders API](https://docs.dinari.com/docs/order-fulfillment-amounts-in-the-orders-api)[Pricing & Quotes](https://docs.dinari.com/docs/pricing-quotes)

Did this page help you?

Yes

No

Copy Page

* + [SDK References](https://docs.dinari.com/docs/stock-data)
  + [SDK Examples](https://docs.dinari.com/docs/stock-data)
  + - [Get list of Stocks](https://docs.dinari.com/docs/stock-data)
    - [Get historical prices for a Stock](https://docs.dinari.com/docs/stock-data)
    - [Get news for a Stock](https://docs.dinari.com/docs/stock-data)
    - [Get live market quote for a Stock](https://docs.dinari.com/docs/stock-data)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Stock Data","dateModified":"2026-11-10T17:53:39.000Z"}
```

<<<PAGE https://docs.dinari.com/docs/pricing-quotes>>>
---
url: https://docs.dinari.com/docs/pricing-quotes
title: Pricing & Quotes
description: Dinari provides realtime prices and quotes for stocks that we cover and it's important to understand the distinction between the two and where this data comes from. Stock Price The realtime stock price is provided by the Get Stock current price API endpoint. This is a singular price denominated in U…
fetched: 2026-11-16
method: static
plan: read
---

## Getting Started

* [Quickstart](https://docs.dinari.com/docs/quickstart)
* [Deploy to production](https://docs.dinari.com/docs/deploy-to-production)
* [Hosted Trading](https://docs.dinari.com/docs/hosted-trading)

## Core Concepts

* [What are dShares™?](https://docs.dinari.com/docs/what-is-dshare)
  + [Blockchain](https://docs.dinari.com/docs/blockchain)
    - [Wrapping dShares™](https://docs.dinari.com/docs/wrapping)
    - [Hyperliquid](https://docs.dinari.com/docs/hyperliquid)
    - [dShare Bridging Guide](https://docs.dinari.com/docs/dshare-bridging-guide)
    - [Deprecation Notices](https://docs.dinari.com/docs/deprecations)
* [What is USD+?](https://docs.dinari.com/docs/what-is-usd)
  + [Blockchain](https://docs.dinari.com/docs/usdplus-evm)
    - [EVM](https://docs.dinari.com/docs/usdplus-evm)
      * [Integration Guide](https://docs.dinari.com/docs/usdplus-evm-integration-guide)
* [Trading Hours](https://docs.dinari.com/docs/trading-hours)
* [Partner Fees](https://docs.dinari.com/docs/fees)

## Technical Integration

* [Entity Management](https://docs.dinari.com/docs/entity-management)
  + [Identity Verification (KYC)](https://docs.dinari.com/docs/managing-kyc)
  + [Managing Accounts](https://docs.dinari.com/docs/managing-accounts)
  + [Managing Wallets](https://docs.dinari.com/docs/managing-wallets)
  + [Funding Accounts through Wallets](https://docs.dinari.com/docs/funding-accounts-through-wallets)
* [Ordering](https://docs.dinari.com/docs/placing-orders)
  + [Placing Orders](https://docs.dinari.com/docs/placing-orders)
    - [Placing dShare Orders with Alchemy](https://docs.dinari.com/docs/placing-dshare-orders-with-alchemy)
    - [Placing dShare Orders with Safe Vaults](https://docs.dinari.com/docs/placing-dshare-orders-with-safe-vaults)
  + [Order Types & Behaviors](https://docs.dinari.com/docs/order-type)
  + [Order Fulfillment Amounts in the Orders API](https://docs.dinari.com/docs/order-fulfillment-amounts-in-the-orders-api)
* [Stock Data](https://docs.dinari.com/docs/stock-data)
  + [Pricing & Quotes](https://docs.dinari.com/docs/pricing-quotes)
  + [24/7 Tradable Assets](https://docs.dinari.com/docs/24-7-trading)
  + [24/5 Tradable Assets](https://docs.dinari.com/docs/245-tradable-assets)
* [Corporate Actions](https://docs.dinari.com/docs/corporate-action-processing)
  + [Dividends](https://docs.dinari.com/docs/dividend-payments)
  + [Stock Splits](https://docs.dinari.com/docs/stock-split-handling)
  + [Ticker Changes](https://docs.dinari.com/docs/ticker-changes)
  + [Mergers](https://docs.dinari.com/docs/mergers)
* [Websockets for Order Data (BETA)](https://docs.dinari.com/docs/websockets)
* [Troubleshooting & Known Issues](https://docs.dinari.com/docs/error-codes)
  + [Error Codes](https://docs.dinari.com/docs/error-codes)
  + [Orders Stuck in SUBMITTED Status](https://docs.dinari.com/docs/stuck-orders)
  + [Smart Contract Wallet Support](https://docs.dinari.com/docs/smart-contract-wallet-support)

## Compliance and Regional

* [Security](https://docs.dinari.com/docs/security)
* [Regional Requirements](https://docs.dinari.com/docs/regional-requirements)
  + [US Customers](https://docs.dinari.com/docs/us)
* [Restrictions](https://docs.dinari.com/docs/restrictions)
* [Taxes & Reporting](https://docs.dinari.com/docs/taxes-reporting)

## Support

* [Staying Safe on Dinari](https://docs.dinari.com/docs/staying-safe-on-dinari)
* [FAQs](https://docs.dinari.com/docs/faqs)
* [Status Pages](https://docs.dinari.com/docs/status-pages)

Powered by

# Pricing & Quotes

Dinari provides realtime prices and quotes for stocks that we cover and it's important to understand the distinction between the two and where this data comes from.

## Stock Price

The realtime stock price is provided by the [Get Stock current price](https://docs.dinari.com/reference-link/getstockcurrentprice) API endpoint. This is a singular price denominated in USD representing the "Fair Market Value" of the stock or what a reasonable price point would be. This number is a computed number blending a number of data points including but not limited to the last trade, recent trade price points/volume and resting order book price points and volume.

This price is what should be used in most cases when displaying to the user.

## Stock Quotes

Realtime stock quotes are provided by the [Get Stock Quote](https://docs.dinari.com/reference-link/getstockcurrentquotesroutev2) API endpoint. Stock quotes represent real interest in buying and selling of the stock. Quotes contain a number of standard components:

* Bid Price: The maximum price buyers are willing to pay
* Bid Volume: # of shares resting at this bid price.
* Ask Price: The minimum price sellers are willing to accept
* Ask Volume: # of shares resting at this ask price.

> 🚧
>
> The stock price will be between the bid and ask price, but might not be the midpoint between the bid and ask prices.

Quotes are best provided at stock pre-confirmation pages and when the user wants to execute a trade. For limit orders, there is a higher chance of execution if the limit price is equal to the bid price for stock sell orders and the ask price for stock buy orders.

## Data Sources

The realtime market data feeds provided by Dinari are included as part of the platform. These included data feeds draw data directly from registered US national exchanges redundantly from multiple sources to deliver the highest quality data possible.

> 📘
>
> Dinari only draws and distributes official US exchange data and does not collect or use data from any purely on-chain trading of dShares™.

> 🚧
>
> IMPORTANT - These feeds only represent a fraction of the total traded stock and may not represent the National Best Bid Offer ("NBBO") data. See the below section regarding realtime SIP data.

### Metered Realtime SIP Data

Realtime Securities Information Processor ("SIP") data is available from Dinari and provides "NBBO" data which represents 100% of traded volume on exchanges. **This data is provided under license**, provided for a fee, and metered per request.

Please reach out to [customer support](https://docs.dinari.com/cdn-cgi/l/email-protection) if you are interested in the realtime SIP data feed.

> 📘
>
> Use of metered realtime SIP data is required for U.S. customers. Please see the US customer integration guide for more details.

### Trading Hours

Another consideration is the trading session. **Dinari operates entirely on regulated US exchanges and ATS's** for the regular, pre-market, post-market and overnight trading sessions. Liquidity available during the pre-market, post-market and overnight trading sessions is significantly lower than regular trading hours. Ensure your users are aware of the increased risk in entering trades during these trading hours.

> 📘
>
> IMPORTANT - It's highly recommended to only make LIMIT orders during this time.

Please see the [Trading Hours](https://docs.dinari.com/docs/trading-hours) page for more information regarding the available trading sessions.

Updated about 1 month ago

---

[Stock Data](https://docs.dinari.com/docs/stock-data)[24/7 Tradable Assets](https://docs.dinari.com/docs/24-7-trading)

Did this page help you?

Yes

No

Copy Page

* + [Stock Price](https://docs.dinari.com/docs/pricing-quotes)
  + [Stock Quotes](https://docs.dinari.com/docs/pricing-quotes)
  + [Data Sources](https://docs.dinari.com/docs/pricing-quotes)
  + - [Metered Realtime SIP Data](https://docs.dinari.com/docs/pricing-quotes)
    - [Trading Hours](https://docs.dinari.com/docs/pricing-quotes)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Pricing & Quotes","dateModified":"2026-10-14T11:29:03.000Z"}
```

<<<PAGE https://docs.dinari.com/docs/stuck-orders>>>
---
url: https://docs.dinari.com/docs/stuck-orders
title: Orders Stuck in SUBMITTED Status
description: Overview / Context In Dinari's system, an order follows a two-stage lifecycle: the OrderRequest (the user's intent) and the Order (the actual on-chain transaction). When an OrderRequest reaches the SUBMITTED status, it means the order has been successfully submitted to the order book and is actively…
fetched: 2026-11-16
method: static
plan: read
---

## Getting Started

* [Quickstart](https://docs.dinari.com/docs/quickstart)
* [Deploy to production](https://docs.dinari.com/docs/deploy-to-production)
* [Hosted Trading](https://docs.dinari.com/docs/hosted-trading)

## Core Concepts

* [What are dShares™?](https://docs.dinari.com/docs/what-is-dshare)
  + [Blockchain](https://docs.dinari.com/docs/blockchain)
    - [Wrapping dShares™](https://docs.dinari.com/docs/wrapping)
    - [Hyperliquid](https://docs.dinari.com/docs/hyperliquid)
    - [dShare Bridging Guide](https://docs.dinari.com/docs/dshare-bridging-guide)
    - [Deprecation Notices](https://docs.dinari.com/docs/deprecations)
* [What is USD+?](https://docs.dinari.com/docs/what-is-usd)
  + [Blockchain](https://docs.dinari.com/docs/usdplus-evm)
    - [EVM](https://docs.dinari.com/docs/usdplus-evm)
      * [Integration Guide](https://docs.dinari.com/docs/usdplus-evm-integration-guide)
* [Trading Hours](https://docs.dinari.com/docs/trading-hours)
* [Partner Fees](https://docs.dinari.com/docs/fees)

## Technical Integration

* [Entity Management](https://docs.dinari.com/docs/entity-management)
  + [Identity Verification (KYC)](https://docs.dinari.com/docs/managing-kyc)
  + [Managing Accounts](https://docs.dinari.com/docs/managing-accounts)
  + [Managing Wallets](https://docs.dinari.com/docs/managing-wallets)
  + [Funding Accounts through Wallets](https://docs.dinari.com/docs/funding-accounts-through-wallets)
* [Ordering](https://docs.dinari.com/docs/placing-orders)
  + [Placing Orders](https://docs.dinari.com/docs/placing-orders)
    - [Placing dShare Orders with Alchemy](https://docs.dinari.com/docs/placing-dshare-orders-with-alchemy)
    - [Placing dShare Orders with Safe Vaults](https://docs.dinari.com/docs/placing-dshare-orders-with-safe-vaults)
  + [Order Types & Behaviors](https://docs.dinari.com/docs/order-type)
  + [Order Fulfillment Amounts in the Orders API](https://docs.dinari.com/docs/order-fulfillment-amounts-in-the-orders-api)
* [Stock Data](https://docs.dinari.com/docs/stock-data)
  + [Pricing & Quotes](https://docs.dinari.com/docs/pricing-quotes)
  + [24/7 Tradable Assets](https://docs.dinari.com/docs/24-7-trading)
  + [24/5 Tradable Assets](https://docs.dinari.com/docs/245-tradable-assets)
* [Corporate Actions](https://docs.dinari.com/docs/corporate-action-processing)
  + [Dividends](https://docs.dinari.com/docs/dividend-payments)
  + [Stock Splits](https://docs.dinari.com/docs/stock-split-handling)
  + [Ticker Changes](https://docs.dinari.com/docs/ticker-changes)
  + [Mergers](https://docs.dinari.com/docs/mergers)
* [Websockets for Order Data (BETA)](https://docs.dinari.com/docs/websockets)
* [Troubleshooting & Known Issues](https://docs.dinari.com/docs/error-codes)
  + [Error Codes](https://docs.dinari.com/docs/error-codes)
  + [Orders Stuck in SUBMITTED Status](https://docs.dinari.com/docs/stuck-orders)
  + [Smart Contract Wallet Support](https://docs.dinari.com/docs/smart-contract-wallet-support)

## Compliance and Regional

* [Security](https://docs.dinari.com/docs/security)
* [Regional Requirements](https://docs.dinari.com/docs/regional-requirements)
  + [US Customers](https://docs.dinari.com/docs/us)
* [Restrictions](https://docs.dinari.com/docs/restrictions)
* [Taxes & Reporting](https://docs.dinari.com/docs/taxes-reporting)

## Support

* [Staying Safe on Dinari](https://docs.dinari.com/docs/staying-safe-on-dinari)
* [FAQs](https://docs.dinari.com/docs/faqs)
* [Status Pages](https://docs.dinari.com/docs/status-pages)

Powered by

# Orders Stuck in SUBMITTED Status

## Overview / Context

In Dinari's system, an order follows a two-stage lifecycle: the OrderRequest (the user's intent) and the Order (the actual on-chain transaction). When an OrderRequest reaches the SUBMITTED status, it means the order has been successfully submitted to the order book and is actively waiting to be matched with a counterparty.

This is a normal and active status — not an error or a stuck state. However, customers frequently perceive it as "stuck" because they expect immediate execution. Understanding why orders remain in SUBMITTED is critical for both support teams and customers to set proper expectations and reduce unnecessary escalations.

---

## Process

### Step 1: Confirm the Order Status

First, verify the order is indeed in SUBMITTED status using the Get Order Request by ID endpoint:

http

`GET /api/v2/accounts/`{account\_id}`/order_requests/`{order\_request\_id}

Look for the status field. If it shows SUBMITTED, the order is active on the order book.

If the stock\_order\_id field is populated, you can also retrieve the Order details:

http

`GET /api/v2/accounts/`{account\_id}`/orders/`{order\_id}

### Step 2: Check the Trading Session

Use the Get Market Hours endpoint to determine the current session:

http

`GET /api/v2/market_data/market_hours/`

Compare the order's created\_dt with the session rules:

| **Session** | **Hours (ET)** | **What It Means for Your Order** |
| --- | --- | --- |
| **Regular** | Weekdays 9:30 AM – 4:00 PM | All order types accepted; expect normal execution |
| **Extended** | Pre-market 4:00–9:30 AM; After-hours 4:00–8:00 PM | Limit orders only; may take longer to fill |
| **Overnight** | 8:00 PM – 4:00 AM weekdays | Limit orders only; fills book in following session |
| **Open (24/7)** | Friday 8:00 PM – Sunday 8:00 PM | Blockchain only; limited tickers; lower liquidity |

#### Step 3: Check the Order Type and TIF

| **Parameter** | **What to Check** |
| --- | --- |
| `order_type` | If `MARKET` and placed off-hours → converted to marketable limit order |
| `order_tif` | If `DAY` and placed over weekend → remains eligible through next trading day |
| `limit_price` | If `LIMIT` order, check if price has been reached |

#### Step 4: Check for Partial Fills

  

Call the Get Order Fulfillments endpoint:

http

`GET /api/v2/accounts/`{account\_id}`/orders/`{order\_id}`/fulfillments`

If any fulfillments exist, the order has been partially filled and is waiting for the remainder.

---

### Key Takeaway

SUBMITTED is not an error state. It's the normal, active state for an order waiting to be filled. Most "stuck" orders are simply resting on the order book during off-hours sessions or waiting for a limit price to be reached. Understanding the trading session rules is the key to setting proper expectations and reducing unnecessary escalations.

Updated about 1 month ago

---

[Websockets for Order Data (BETA)](https://docs.dinari.com/docs/websockets)[Smart Contract Wallet Support](https://docs.dinari.com/docs/smart-contract-wallet-support)

Did this page help you?

Yes

No

Copy Page

* + [Overview / Context](https://docs.dinari.com/docs/stuck-orders)
  + [Process](https://docs.dinari.com/docs/stuck-orders)
  + - [Step 1: Confirm the Order Status](https://docs.dinari.com/docs/stuck-orders)
    - [Step 2: Check the Trading Session](https://docs.dinari.com/docs/stuck-orders)
    - * [Step 3: Check the Order Type and TIF](https://docs.dinari.com/docs/stuck-orders)
      * [Step 4: Check for Partial Fills](https://docs.dinari.com/docs/stuck-orders)
    - [Key Takeaway](https://docs.dinari.com/docs/stuck-orders)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Orders Stuck in SUBMITTED Status","dateModified":"2026-10-14T11:54:48.000Z"}
```

<<<PAGE https://docs.dinari.com/docs/websockets>>>
---
url: https://docs.dinari.com/docs/websockets
title: Websockets for Order Data (BETA)
description: Subscribe to real-time market data and order updates via websockets.
fetched: 2026-11-16
method: static
plan: read
---

## Getting Started

* [Quickstart](https://docs.dinari.com/docs/quickstart)
* [Deploy to production](https://docs.dinari.com/docs/deploy-to-production)
* [Hosted Trading](https://docs.dinari.com/docs/hosted-trading)

## Core Concepts

* [What are dShares™?](https://docs.dinari.com/docs/what-is-dshare)
  + [Blockchain](https://docs.dinari.com/docs/blockchain)
    - [Wrapping dShares™](https://docs.dinari.com/docs/wrapping)
    - [Hyperliquid](https://docs.dinari.com/docs/hyperliquid)
    - [dShare Bridging Guide](https://docs.dinari.com/docs/dshare-bridging-guide)
    - [Deprecation Notices](https://docs.dinari.com/docs/deprecations)
* [What is USD+?](https://docs.dinari.com/docs/what-is-usd)
  + [Blockchain](https://docs.dinari.com/docs/usdplus-evm)
    - [EVM](https://docs.dinari.com/docs/usdplus-evm)
      * [Integration Guide](https://docs.dinari.com/docs/usdplus-evm-integration-guide)
* [Trading Hours](https://docs.dinari.com/docs/trading-hours)
* [Partner Fees](https://docs.dinari.com/docs/fees)

## Technical Integration

* [Entity Management](https://docs.dinari.com/docs/entity-management)
  + [Identity Verification (KYC)](https://docs.dinari.com/docs/managing-kyc)
  + [Managing Accounts](https://docs.dinari.com/docs/managing-accounts)
  + [Managing Wallets](https://docs.dinari.com/docs/managing-wallets)
  + [Funding Accounts through Wallets](https://docs.dinari.com/docs/funding-accounts-through-wallets)
* [Ordering](https://docs.dinari.com/docs/placing-orders)
  + [Placing Orders](https://docs.dinari.com/docs/placing-orders)
    - [Placing dShare Orders with Alchemy](https://docs.dinari.com/docs/placing-dshare-orders-with-alchemy)
    - [Placing dShare Orders with Safe Vaults](https://docs.dinari.com/docs/placing-dshare-orders-with-safe-vaults)
  + [Order Types & Behaviors](https://docs.dinari.com/docs/order-type)
  + [Order Fulfillment Amounts in the Orders API](https://docs.dinari.com/docs/order-fulfillment-amounts-in-the-orders-api)
* [Stock Data](https://docs.dinari.com/docs/stock-data)
  + [Pricing & Quotes](https://docs.dinari.com/docs/pricing-quotes)
  + [24/7 Tradable Assets](https://docs.dinari.com/docs/24-7-trading)
  + [24/5 Tradable Assets](https://docs.dinari.com/docs/245-tradable-assets)
* [Corporate Actions](https://docs.dinari.com/docs/corporate-action-processing)
  + [Dividends](https://docs.dinari.com/docs/dividend-payments)
  + [Stock Splits](https://docs.dinari.com/docs/stock-split-handling)
  + [Ticker Changes](https://docs.dinari.com/docs/ticker-changes)
  + [Mergers](https://docs.dinari.com/docs/mergers)
* [Websockets for Order Data (BETA)](https://docs.dinari.com/docs/websockets)
* [Troubleshooting & Known Issues](https://docs.dinari.com/docs/error-codes)
  + [Error Codes](https://docs.dinari.com/docs/error-codes)
  + [Orders Stuck in SUBMITTED Status](https://docs.dinari.com/docs/stuck-orders)
  + [Smart Contract Wallet Support](https://docs.dinari.com/docs/smart-contract-wallet-support)

## Compliance and Regional

* [Security](https://docs.dinari.com/docs/security)
* [Regional Requirements](https://docs.dinari.com/docs/regional-requirements)
  + [US Customers](https://docs.dinari.com/docs/us)
* [Restrictions](https://docs.dinari.com/docs/restrictions)
* [Taxes & Reporting](https://docs.dinari.com/docs/taxes-reporting)

## Support

* [Staying Safe on Dinari](https://docs.dinari.com/docs/staying-safe-on-dinari)
* [FAQs](https://docs.dinari.com/docs/faqs)
* [Status Pages](https://docs.dinari.com/docs/status-pages)

Powered by

# Websockets for Order Data (BETA)

Subscribe to real-time market data and order updates via websockets.

> ⚠️
>
> ### DRAFT
>
> The websocket feature is currently in **beta** and the implementation may change.

Dinari's Websocket API provides real-time market data and order updates, allowing you to receive instant pricing and quotes as well as notifications about order status changes, fulfillments, and other order-related events without polling the REST API.

# Key Features

* **Real-time Updates**: Receive order status changes as they happen
* **Efficient**: Eliminate the need for constant polling of the REST API
* **Scalable**: Handle multiple subscriptions per connection
* **Reliable**: Automatic reconnection and message acknowledgments

# Usage

| Environment | Hostname |
| --- | --- |
| Production | `wss://ws.api.dinari.com` |
| Sandbox | `wss://ws.api.sandbox.dinari.com` **(coming soon)** |

## Authentication

WebSocket connections require authentication using your API credentials. Please use the correct credentials for your environment (sandbox or production).

**Authentication Request**

JSON

```
{
  "command": "authenticate",
  "data": {
    "api_key": "your api key",
    "api_secret": "your api key secret"
  }
}
```

**Response**

JSON

```
{
  "event_type": "authentication",
  "data": {
    "status": "authenticated",
    "entity_id": "0197422f-d3cb-7050-ae5f-e5b9473f067b"
  }
}
```

## Market Data

| Available Data Types | Description |
| --- | --- |
| `stock_dfn_l2` | DFN Level 2 order book data |
| `stock_dfn_quotes` | DFN top-of-book quotes |

**Subscription**

Subscribe to market data with the `market_data_subscribe` command. This command may be reissued at anytime to update the subscription. All requested `stock_ids` must be listed.

> `stock_ids` can be fetched from the [🔗 Get Stocks](https://docs.dinari.com/reference/getstocks) API endpoint.

JSON

```
{
  "command": "market_data_subscribe",
  "data": {
    "stock_dfn_l2": ["stock_id or * for all"], 
    "stock_dfn_quotes": ["stock_id or * for all"]
  }
}
```

### Data Types

**Level 2 Data**

JSON

```
{
  "event_type": "market_data:l2_data",
  "data": {
    "Symbol": "AAPL",
    "MaxDepth": 30,
    "Bids": [
      {
        "Price": 0.01,
        "Size": 150,
        "Depth": 1,
        "NumOrders": 1
      }
    ],
    "Asks": [],
    "LastMatch": null,
    "Timestamp": "2025-12-12T17:54:44.382483808Z",
    "SchemaVersion": "1.0.0"
  }
}
```

**DFN Quote**

JSON

```
{
  "event_type": "market_data:dfn_quote",
  "data": {
    "Symbol": "AAPL",
    "BidExchange": "DFN",
    "BidPrice": 0.01,
    "BidSize": 150,
    "AskExchange": "DFN",
    "AskPrice": 0,
    "AskSize": 0,
    "TimeStamp": "2025-12-11T17:17:54.141119146Z",
    "Conditions": null,
    "Tape": ""
  }
}
```

## Order Data

Use the `order_data_subscribe` command with an empty data map to subscribe to real-time updates for your customer's orders account.

> ⚠️
>
> ### Cursor support coming soon

**Subscription Request**

JSON

```
{
  "command": "order_data_subscribe",
  "data": {}
}
```

**Response**

JSON

```
{
  "event_type": "order_data_subscription",
  "data": {
    "status": "subscribed"
  }
}
```

### Data Types

**Order Request**

JSON

```
{
  "event_type": "order_data",
  "data": {
    "entity_id": "0197422f-d3cb-7050-ae5f-e5b9473f067b",
    "order_request": {
      "id": "019b1384-2fc9-7485-ab0b-01eefe126151",
      "account_id": "0198862c-61ec-7375-bd98-4e306ab177c9",
      "recipient_account_id": "0198862c-61ec-7375-bd98-4e306ab177c9",
      "status": "QUOTED",
      "order_side": "SELL",
      "order_type": "LIMIT",
      "order_tif": "DAY",
      "order_id": null,
      "created_dt": "2025-12-12T17:03:08.724979Z"
    }
  }
}
```

**Order Data**

JSON

```
{
  "event_type": "order_data",
  "data": {
    "entity_id": "0197422f-d3cb-7050-ae5f-e5b9473f067b",
    "order": {
      "id": "019b1385-3b4b-711e-b039-070ac42ea918",
      "status": "SUBMITTED",
      "order_contract_address": "0x1f96D1656a6500e526E92B19EAA894A6A7647ABa",
      "order_transaction_hash": "0x0e36a82c5fe36075f2badc1b787ffc929a317a8ce02200ef4c72a95e46c70e29",
      "cancel_transaction_hash": null,
      "order_side": "SELL",
      "order_type": "LIMIT",
      "order_tif": "DAY",
      "order_request_id": "019b1384-2fc9-7485-ab0b-01eefe126151",
      "stock_id": "0196d545-d8a8-7210-8cd1-a49e82c31e53",
      "asset_token_quantity": 0.001000000000000000,
      "payment_token_quantity": 0,
      "payment_token": "0xd54c40022500D88BbE0262FA9ffdf3D9921B24e8",
      "limit_price": 100.000000000000000000,
      "created_dt": "2025-12-12T17:04:17.223274Z",
      "chain_id": "eip155:202110",
      "asset_token": "0x83EBfbC73e60c45380426acc66725405A4EF7D61",
      "fees": 0
    }
  }
}
```

**Order Fulfillment**

JSON

```
{
  "event_type": "order_data",
  "data": {
    "entity_id": "0197422f-d3cb-7050-ae5f-e5b9473f067b",
    "order_fulfillment": {
      "id": "019b1385-3b4b-711e-b039-070ac42ea918",
      "order_id": "019b1385-3b4b-711e-b039-070ac42ea918",
      "chain_id": "eip155:202110",
      "transaction_hash": "0xc488f4fcc8ee5163766935dfba7cf6b50a862b67eeeda7e01b6d5dab59746c2f",
      "transaction_dt": "2025-12-12T17:04:17.223274Z",
      "asset_token_filled": 0,
      "asset_token_spent": 0.001,
      "payment_token_filled": 0.279014000000000000,
      "payment_token_spent": 0,
      "payment_token_fee": 0.201395070000000000
    }
  }
}
```

Updated 10 days ago

---

[Mergers](https://docs.dinari.com/docs/mergers)[Troubleshooting & Known Issues](https://docs.dinari.com/docs/troubleshooting-known-issues)

Did this page help you?

Yes

No

Copy Page

* + [Key Features](https://docs.dinari.com/docs/websockets)
  + [Usage](https://docs.dinari.com/docs/websockets)
  + - [Authentication](https://docs.dinari.com/docs/websockets)
    - [Market Data](https://docs.dinari.com/docs/websockets)
    - * [Data Types](https://docs.dinari.com/docs/websockets)
    - [Order Data](https://docs.dinari.com/docs/websockets)
    - * [Data Types](https://docs.dinari.com/docs/websockets)

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Websockets for Order Data (BETA)","dateModified":"2026-11-06T16:53:49.000Z"}
```

<<<PAGE https://docs.dinari.com/docs/smart-contract-wallet-support>>>
---
url: https://docs.dinari.com/docs/smart-contract-wallet-support
title: Smart Contract Wallet Support
description: 
fetched: 2026-11-16
method: static
plan: read
---

## Getting Started

* [Quickstart](https://docs.dinari.com/docs/quickstart)
* [Deploy to production](https://docs.dinari.com/docs/deploy-to-production)
* [Hosted Trading](https://docs.dinari.com/docs/hosted-trading)

## Core Concepts

* [What are dShares™?](https://docs.dinari.com/docs/what-is-dshare)
  + [Blockchain](https://docs.dinari.com/docs/blockchain)
    - [Wrapping dShares™](https://docs.dinari.com/docs/wrapping)
    - [Hyperliquid](https://docs.dinari.com/docs/hyperliquid)
    - [dShare Bridging Guide](https://docs.dinari.com/docs/dshare-bridging-guide)
    - [Deprecation Notices](https://docs.dinari.com/docs/deprecations)
* [What is USD+?](https://docs.dinari.com/docs/what-is-usd)
  + [Blockchain](https://docs.dinari.com/docs/usdplus-evm)
    - [EVM](https://docs.dinari.com/docs/usdplus-evm)
      * [Integration Guide](https://docs.dinari.com/docs/usdplus-evm-integration-guide)
* [Trading Hours](https://docs.dinari.com/docs/trading-hours)
* [Partner Fees](https://docs.dinari.com/docs/fees)

## Technical Integration

* [Entity Management](https://docs.dinari.com/docs/entity-management)
  + [Identity Verification (KYC)](https://docs.dinari.com/docs/managing-kyc)
  + [Managing Accounts](https://docs.dinari.com/docs/managing-accounts)
  + [Managing Wallets](https://docs.dinari.com/docs/managing-wallets)
  + [Funding Accounts through Wallets](https://docs.dinari.com/docs/funding-accounts-through-wallets)
* [Ordering](https://docs.dinari.com/docs/placing-orders)
  + [Placing Orders](https://docs.dinari.com/docs/placing-orders)
    - [Placing dShare Orders with Alchemy](https://docs.dinari.com/docs/placing-dshare-orders-with-alchemy)
    - [Placing dShare Orders with Safe Vaults](https://docs.dinari.com/docs/placing-dshare-orders-with-safe-vaults)
  + [Order Types & Behaviors](https://docs.dinari.com/docs/order-type)
  + [Order Fulfillment Amounts in the Orders API](https://docs.dinari.com/docs/order-fulfillment-amounts-in-the-orders-api)
* [Stock Data](https://docs.dinari.com/docs/stock-data)
  + [Pricing & Quotes](https://docs.dinari.com/docs/pricing-quotes)
  + [24/7 Tradable Assets](https://docs.dinari.com/docs/24-7-trading)
  + [24/5 Tradable Assets](https://docs.dinari.com/docs/245-tradable-assets)
* [Corporate Actions](https://docs.dinari.com/docs/corporate-action-processing)
  + [Dividends](https://docs.dinari.com/docs/dividend-payments)
  + [Stock Splits](https://docs.dinari.com/docs/stock-split-handling)
  + [Ticker Changes](https://docs.dinari.com/docs/ticker-changes)
  + [Mergers](https://docs.dinari.com/docs/mergers)
* [Websockets for Order Data (BETA)](https://docs.dinari.com/docs/websockets)
* [Troubleshooting & Known Issues](https://docs.dinari.com/docs/error-codes)
  + [Error Codes](https://docs.dinari.com/docs/error-codes)
  + [Orders Stuck in SUBMITTED Status](https://docs.dinari.com/docs/stuck-orders)
  + [Smart Contract Wallet Support](https://docs.dinari.com/docs/smart-contract-wallet-support)

## Compliance and Regional

* [Security](https://docs.dinari.com/docs/security)
* [Regional Requirements](https://docs.dinari.com/docs/regional-requirements)
  + [US Customers](https://docs.dinari.com/docs/us)
* [Restrictions](https://docs.dinari.com/docs/restrictions)
* [Taxes & Reporting](https://docs.dinari.com/docs/taxes-reporting)

## Support

* [Staying Safe on Dinari](https://docs.dinari.com/docs/staying-safe-on-dinari)
* [FAQs](https://docs.dinari.com/docs/faqs)
* [Status Pages](https://docs.dinari.com/docs/status-pages)

Powered by

# Smart Contract Wallet Support

Copy Page

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Smart Contract Wallet Support","dateModified":"2026-10-14T11:31:27.000Z"}
```

<<<PAGE https://docs.dinari.com/docs>>>
(본문이 https://docs.dinari.com/ 과 같아 생략)

<<<PAGE https://docs.dinari.com/docs/error-codes>>>
---
url: https://docs.dinari.com/docs/error-codes
title: Error Codes
description: 
fetched: 2026-11-16
method: static
plan: read
---

## Getting Started

* [Quickstart](https://docs.dinari.com/docs/quickstart)
* [Deploy to production](https://docs.dinari.com/docs/deploy-to-production)
* [Hosted Trading](https://docs.dinari.com/docs/hosted-trading)

## Core Concepts

* [What are dShares™?](https://docs.dinari.com/docs/what-is-dshare)
  + [Blockchain](https://docs.dinari.com/docs/blockchain)
    - [Wrapping dShares™](https://docs.dinari.com/docs/wrapping)
    - [Hyperliquid](https://docs.dinari.com/docs/hyperliquid)
    - [dShare Bridging Guide](https://docs.dinari.com/docs/dshare-bridging-guide)
    - [Deprecation Notices](https://docs.dinari.com/docs/deprecations)
* [What is USD+?](https://docs.dinari.com/docs/what-is-usd)
  + [Blockchain](https://docs.dinari.com/docs/usdplus-evm)
    - [EVM](https://docs.dinari.com/docs/usdplus-evm)
      * [Integration Guide](https://docs.dinari.com/docs/usdplus-evm-integration-guide)
* [Trading Hours](https://docs.dinari.com/docs/trading-hours)
* [Partner Fees](https://docs.dinari.com/docs/fees)

## Technical Integration

* [Entity Management](https://docs.dinari.com/docs/entity-management)
  + [Identity Verification (KYC)](https://docs.dinari.com/docs/managing-kyc)
  + [Managing Accounts](https://docs.dinari.com/docs/managing-accounts)
  + [Managing Wallets](https://docs.dinari.com/docs/managing-wallets)
  + [Funding Accounts through Wallets](https://docs.dinari.com/docs/funding-accounts-through-wallets)
* [Ordering](https://docs.dinari.com/docs/placing-orders)
  + [Placing Orders](https://docs.dinari.com/docs/placing-orders)
    - [Placing dShare Orders with Alchemy](https://docs.dinari.com/docs/placing-dshare-orders-with-alchemy)
    - [Placing dShare Orders with Safe Vaults](https://docs.dinari.com/docs/placing-dshare-orders-with-safe-vaults)
  + [Order Types & Behaviors](https://docs.dinari.com/docs/order-type)
  + [Order Fulfillment Amounts in the Orders API](https://docs.dinari.com/docs/order-fulfillment-amounts-in-the-orders-api)
* [Stock Data](https://docs.dinari.com/docs/stock-data)
  + [Pricing & Quotes](https://docs.dinari.com/docs/pricing-quotes)
  + [24/7 Tradable Assets](https://docs.dinari.com/docs/24-7-trading)
  + [24/5 Tradable Assets](https://docs.dinari.com/docs/245-tradable-assets)
* [Corporate Actions](https://docs.dinari.com/docs/corporate-action-processing)
  + [Dividends](https://docs.dinari.com/docs/dividend-payments)
  + [Stock Splits](https://docs.dinari.com/docs/stock-split-handling)
  + [Ticker Changes](https://docs.dinari.com/docs/ticker-changes)
  + [Mergers](https://docs.dinari.com/docs/mergers)
* [Websockets for Order Data (BETA)](https://docs.dinari.com/docs/websockets)
* [Troubleshooting & Known Issues](https://docs.dinari.com/docs/error-codes)
  + [Error Codes](https://docs.dinari.com/docs/error-codes)
  + [Orders Stuck in SUBMITTED Status](https://docs.dinari.com/docs/stuck-orders)
  + [Smart Contract Wallet Support](https://docs.dinari.com/docs/smart-contract-wallet-support)

## Compliance and Regional

* [Security](https://docs.dinari.com/docs/security)
* [Regional Requirements](https://docs.dinari.com/docs/regional-requirements)
  + [US Customers](https://docs.dinari.com/docs/us)
* [Restrictions](https://docs.dinari.com/docs/restrictions)
* [Taxes & Reporting](https://docs.dinari.com/docs/taxes-reporting)

## Support

* [Staying Safe on Dinari](https://docs.dinari.com/docs/staying-safe-on-dinari)
* [FAQs](https://docs.dinari.com/docs/faqs)
* [Status Pages](https://docs.dinari.com/docs/status-pages)

Powered by

# Error Codes

Copy Page

## 구조화 데이터(JSON-LD)

```json
{"@context":"https://schema.org","@type":"TechArticle","headline":"Error Codes","dateModified":"2026-10-14T11:30:38.000Z"}
```

## 훑기 대상(같은 틀의 페이지 묶음): 조사 질문과 관련 있으면 read로 올려 다시 수집

| URL | 제목 | 첫머리 |
|---|---|---|
| https://docs.dinari.com/docs/kinto-deprecation |  |  |
| https://docs.dinari.com/docs/getting-started | Quickstart | ## Getting Started * [Quickstart](https://docs.dinari.com/docs/quickstart) * [Deploy to production](https://docs.dinari.com/docs/deploy-to-production) * [Hosted Trading](https://docs.dinari.com/docs/hosted-trading) ## Core Concepts * [What  |
| https://docs.dinari.com/docs/dshare-ordering | Placing Orders | ## Getting Started * [Quickstart](https://docs.dinari.com/docs/quickstart) * [Deploy to production](https://docs.dinari.com/docs/deploy-to-production) * [Hosted Trading](https://docs.dinari.com/docs/hosted-trading) ## Core Concepts * [What  |
| https://docs.dinari.com/docs/placing-dshare-orders |  |  |
| https://docs.dinari.com/docs/support@dinari.com |  |  |
| https://docs.dinari.com/docs/troubleshooting-known-issues | Error Codes | ## Getting Started * [Quickstart](https://docs.dinari.com/docs/quickstart) * [Deploy to production](https://docs.dinari.com/docs/deploy-to-production) * [Hosted Trading](https://docs.dinari.com/docs/hosted-trading) ## Core Concepts * [What  |
| https://docs.dinari.com/docs/blockchain-1 | EVM | ## Getting Started * [Quickstart](https://docs.dinari.com/docs/quickstart) * [Deploy to production](https://docs.dinari.com/docs/deploy-to-production) * [Hosted Trading](https://docs.dinari.com/docs/hosted-trading) ## Core Concepts * [What  |
