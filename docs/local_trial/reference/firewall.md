Tabular AI Firewall Realtime
============================

The AI Firewall depends on two important components for configuration:
1. The corresponding [stress test configuration](/for_data_scientists/reference/tabular/stress_testing.md)
2. An additional Firewall Rule JSON Configuration file.


The JSON configuration file is auto-generated from a stress test run. It contains
some configuration parameters that are learned from your data and model during
stress testing. These configuration parameters include:
- The configured firewall action
- The estimated performance impact of each firewall rule
- The set of feature columns for each rule.

The configuration file is not meant to be edited directly.
Configuration of actions is done through the Firewall class itself.
The configuration can be viewed through the UI in the "Firewall Configuration"
screen.

<img src="../../_static/ui/FirewallConfig_RulesDetail.png" />

Clicking on a rule will give more details regarding the features the rule is configured over
as well as the estimated performance change for each feature.
<img src="../../_static/ui/FirewallConfig_RulesDetailExpand.png" />