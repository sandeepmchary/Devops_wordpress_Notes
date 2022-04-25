Devops Classroom 23/0ct/2019
Primary reference
- Overview
## SLI(Service Level Indicator)
> Indicator of Availability of your applications/mobile
>Sample Indicators:
	> Latency of home page over 5 minutes will be less than 300ms for 99.9% of the requests

## SLO (Service Level Objective)
 > SLI binds over a period of time
 > Sample:
	> Latency of home page over a year will be less than 300ms for 99.9% of the requests


## SLA(Service Level Agreements)	
> Sample:
	> Customers will be offered free credits if 99.5 % of the requests over a year fail to achieved the latency of less than 300ms 

## Problem:
> We build systems and they will fail at some point
> Whats's the SRE approach towards failure

## Risks:
> You can make aggressive deployments as long as you are with in the Error Budget
> If Error Budger is exceeded no more deployments

## Error Budget:
> Allowed time in minutes or hours of failure.
> Sample:
		> SLO: Latency will be less than 300ms for 99.9% of request over the year
		> ERROR Budget is what is left of total time after removing SLO (100-99.9)*365*24*60/100=525.6 minutes/year
		> SLO: Latency will be less than 300ms for 99.99% of request over the year
		> Error Budget (100-99)*365*24*60/100=52.5 minutes/year
## ERROR BUDGET BURNDOWN
> Error Budget used
> Fast Burndown
> Slow Burndown

## TOIL:
> Repetitive manual work that can be automated
> Focus on Toils which are more frequent than infrequent ones

		