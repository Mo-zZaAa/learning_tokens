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