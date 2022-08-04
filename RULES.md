# Architecture Game Rules

## Layers
1. Network Layer
   * Load Balancers
2. Code Layer
   * App Servers
3. Data Layer
   * Databases
   * Read through caches

## Topology Rules
1. Customer connection must go to an app server OR through a load balancer to multiple app servers.
2. All transactions must go through an app server and down to the data layer.
3. An app server can connect to either a database or a read through cache.
4. Multiple app servers can connect to either a database or a read through cache. 
5. A load balancer is required for more than one app server, but is not limited in how many app servers it can support.
6. A read through cache must connect to a database and can only be used in a READ transaction.
7. A database is required for a WRITE transaction.
8. Multiple components must all be the same level, i.e. all level 1 or all level 2.

## Scoring
1. Scores are calculated separately for both READ & WRITE transactions.
2. WRITE transactions are worth twice READ transactions.
3. Throughput equals the minimum of the total for each layer.
4. Latency equals the sum of the average latency for READ or WRITE on a layer.
5. Score is equal to throughput over latency in seconds (x 1000)
6. Total additional budget for the next round is score to the nearest $5.

## Game Play

1. Start with $100 daily budget
2. Purchase servers
3. Calculate score for the round (round 1), receive additional budget
4. Spend the additional budget or skip straight to calculating the score (round 2).
5. On even rounds pick up a chance card before calculating the score.

## Example

Round 1 (initial $100 to spend):
   - 1 x L1 Load Balancer ($50)
   - 2 x L1 App Servers (2x $15)
   - 1 x L1 Database Server ($20)

READ Score:
   - Throughput = Min( 2000m/s [LB], 2x 250m/s [AS], 1000m/s [DB] ) = 500m/s
   - Latency = Sum( 200ms [LB], AVG(200ms 200ms) == 200ms [AS], 400ms [DB] ) = 800ms
   - Score = 500m/s / 0.8s = 62.5

WRITE Score:
   - Score = 2x READ Score = 125

Total additional budget: $190 ($187.5 >> $5)