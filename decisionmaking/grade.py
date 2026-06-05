"""
Champions/High Spenders (Score 80-100): These are top-tier customers who spend frequently and heavily. They are brand advocates and early adopters.
High Potential/Active Loyalists (Score 60-80): These customers have a high spending score and are recent buyers, but they may not purchase as frequently as champions. They are prime candidates for loyalty programs.
Moderate/Average Spenders (Score 40-60): These customers spend at a steady, average rate. They make up a large portion of the base and can be targeted with engagement campaigns to increase their spending.
Low Spenders/Occasional Shoppers (Score 20-40): These customers spend occasionally and have low overall engagement. They may need incentives or better product variety to spend more.
Inactive/Lost Customers (Score 1-20): These customers have not made a purchase in a long time and have a very low spending score
"""

spending_score  = int(input("enter spending score.."))


# 100-80

if spending_score<=100 and spending_score>80:

    print("Champions")

elif spending_score<=80 and spending_score>60:

    print("High Potential/Active Loyalists")

elif spending_score<=60 and spending_score>40:

    print("Moderate/Average Spenders ")

elif spending_score<=40 and spending_score>20:

    print("Low Spenders/Occasional Shoppers")

elif spending_score<=20 and spending_score>1:

    print("Inactive/Lost Customers")

else:
    print("invalid spending score")

