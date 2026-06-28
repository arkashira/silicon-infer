# breakeven.md

## Unit Economics & Break-even Analysis

### Cost per Active User
- **Compute Costs**: 
  - Average cost for Apple Silicon optimized inference: $0.10 per t/s.
  - Target throughput: 200 t/s.
  - Monthly compute cost per user: $0.10 * 200 t/s * 720 hours = **$1,440**.

- **Storage Costs**: 
  - Average storage cost for model and data: $0.02 per GB.
  - Estimated storage per user: 10 GB.
  - Monthly storage cost per user: $0.02 * 10 GB = **$0.20**.

- **Bandwidth Costs**: 
  - Average bandwidth cost: $0.01 per GB.
  - Estimated bandwidth usage per user: 50 GB.
  - Monthly bandwidth cost per user: $0.01 * 50 GB = **$0.50**.

- **Total Cost per Active User**: 
  - Compute + Storage + Bandwidth = $1,440 + $0.20 + $0.50 = **$1,440.70**.

### Pricing Tiers
1. **Basic Tier**: $49/month
   - Features: Access to local coding model, basic support, community forum access.
  
2. **Pro Tier**: $99/month
   - Features: Access to local coding model, priority support, advanced features (e.g., enhanced reasoning capabilities), community forum access.

3. **Enterprise Tier**: $199/month
   - Features: Access to local coding model, dedicated support, custom integrations, advanced analytics, community forum access.

### Customer Acquisition Cost (CAC) Range
- Estimated CAC: **$300 - $500** per user.
  - This includes marketing, sales, and onboarding costs.

### Lifetime Value (LTV) Estimate
- Average user retention: 24 months.
- LTV = Monthly Revenue per User * Average Retention Period.
- For Basic Tier: $49 * 24 = **$1,176**.
- For Pro Tier: $99 * 24 = **$2,376**.
- For Enterprise Tier: $199 * 24 = **$4,776**.

### Break-even Users Count
- Break-even point = Total Costs / (Price per User - CAC).
- For Basic Tier: 
  - Break-even users = $1,440.70 / ($49 - $300) = **Not feasible**.
  
- For Pro Tier: 
  - Break-even users = $1,440.70 / ($99 - $300) = **Not feasible**.
  
- For Enterprise Tier: 
  - Break-even users = $1,440.70 / ($199 - $500) = **Not feasible**.

### Path to $10K MRR
- Target MRR: $10,000.
- Assuming all users are on the Enterprise Tier ($199/month):
  - Required users = $10,000 / $199 = **50.25 users** (round up to 51 users).

- If targeting the Pro Tier ($99/month):
  - Required users = $10,000 / $99 = **101.01 users** (round up to 102 users).

- If targeting the Basic Tier ($49/month):
  - Required users = $10,000 / $49 = **204.08 users** (round up to 205 users).

### Summary
- **Total Cost per Active User**: $1,440.70
- **Pricing Tiers**: Basic ($49), Pro ($99), Enterprise ($199)
- **CAC Range**: $300 - $500
- **LTV Estimates**: Basic ($1,176), Pro ($2,376), Enterprise ($4,776)
- **Break-even Users Count**: Not feasible under current pricing.
- **Path to $10K MRR**: 51 Enterprise users, 102 Pro users, or 205 Basic users.