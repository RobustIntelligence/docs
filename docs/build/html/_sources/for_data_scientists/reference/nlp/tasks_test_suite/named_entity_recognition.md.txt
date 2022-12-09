### Named Entity Recognition Testing Config


Below is the default configuration for all Named Entity Recognition tests. A copy of this can also be found in your `rime_trial` bundle (inside the `nlp_examples/ner/default_test_config.json`).

```python
{
  "categories": [],
  "run_default": null,
  "custom_tests": null,
  "dynamic_configs": {},
  "numeric_outlier": {
    "exclude_columns": [],
    "run": false,
    "performance_change_config": {
      "severity_thresholds": null,
      "min_num_samples": 1
    },
    "min_normal_prop": 0.99,
    "baseline_quantile": 0.1,
    "perturb_multiplier": 1.0
  },
  "unseen_categorical": {
    "exclude_columns": [],
    "run": false,
    "performance_change_config": {
      "severity_thresholds": null,
      "min_num_samples": 1
    }
  },
  "unseen_domain": {
    "exclude_columns": [],
    "run": false,
    "performance_change_config": {
      "severity_thresholds": null,
      "min_num_samples": 1
    }
  },
  "unseen_email": {
    "exclude_columns": [],
    "run": false,
    "performance_change_config": {
      "severity_thresholds": null,
      "min_num_samples": 1
    }
  },
  "unseen_url": {
    "exclude_columns": [],
    "run": false,
    "performance_change_config": {
      "severity_thresholds": null,
      "min_num_samples": 1
    }
  },
  "rare_categories": {
    "exclude_columns": [],
    "run": false,
    "performance_change_config": {
      "severity_thresholds": null,
      "min_num_samples": 1
    },
    "include_columns": [],
    "min_num_occurrences": 0,
    "min_pct_occurrences": 0,
    "min_ratio_rel_uniform": 0.005
  },
  "out_of_range": {
    "exclude_columns": [],
    "run": false,
    "performance_change_config": {
      "severity_thresholds": null,
      "min_num_samples": 1
    },
    "std_factor": 3
  },
  "req_characters": {
    "column_specific_params": {},
    "exclude_columns": [],
    "run": false,
    "performance_change_config": {
      "severity_thresholds": null,
      "min_num_samples": 1
    }
  },
  "inconsistencies": {
    "exclude_columns": [],
    "run": false,
    "performance_change_config": {
      "severity_thresholds": null,
      "min_num_samples": 1
    },
    "freq_ratio_threshold": 0.02,
    "min_correlation": 0.1,
    "max_pairwise_tests": 200,
    "max_unique_pairs_for_firewall": 15
  },
  "capitalization": {
    "exclude_columns": [],
    "run": false,
    "performance_change_config": {
      "severity_thresholds": null,
      "min_num_samples": 1
    }
  },
  "empty_string": {
    "exclude_columns": [],
    "run": false,
    "performance_change_config": {
      "severity_thresholds": null,
      "min_num_samples": 1
    }
  },
  "embedding_anomalies": {
    "exclude_columns": [],
    "run": false,
    "performance_change_config": {
      "severity_thresholds": null,
      "min_num_samples": 1
    },
    "distance_quantile": 0.995
  },
  "correlation_feat_drift": {
    "exclude_columns": [],
    "run": false,
    "correlation_drift_thresholds": [
      0.3,
      0.5,
      0.7
    ],
    "p_value_threshold": 0.05,
    "min_correlation": 0.1,
    "max_pairwise_tests": 200
  },
  "correlation_label_drift": {
    "exclude_columns": [],
    "run": false,
    "correlation_drift_thresholds": [
      0.3,
      0.5,
      0.7
    ],
    "p_value_threshold": 0.05
  },
  "mutual_information_feat_drift": {
    "exclude_columns": [],
    "run": false,
    "min_mutual_information": 0.1,
    "mutual_information_thresholds": [
      0.1,
      0.2,
      0.3
    ],
    "max_pairwise_tests": 200,
    "min_sample_size": 100
  },
  "mutual_information_label_drift": {
    "exclude_columns": [],
    "run": false,
    "mutual_information_thresholds": [
      0.1,
      0.2,
      0.3
    ]
  },
  "categorical_label_drift": {
    "run": false,
    "drift_statistic": "Population Stability Index",
    "params": {
      "psi_thresholds": [
        0.2,
        0.4,
        0.6
      ]
    }
  },
  "multiclass_pred_label_drift": {
    "run": false,
    "drift_statistic": "Population Stability Index",
    "params": {
      "psi_thresholds": [
        0.2,
        0.4,
        0.6
      ]
    }
  },
  "regression_label_drift": {
    "run": false,
    "drift_statistic": "Population Stability Index",
    "params": {
      "psi_thresholds": [
        0.2,
        0.4,
        0.6
      ],
      "num_bins": 100
    }
  },
  "categorical_drift": {
    "exclude_columns": [],
    "run": false,
    "min_sample_size": 100,
    "performance_change_thresholds": null,
    "max_sample_size": null,
    "drift_statistic": "Population Stability Index",
    "params": {
      "distance_threshold": 0.2
    },
    "ignore_nans": true
  },
  "continuous_drift": {
    "exclude_columns": [],
    "run": false,
    "min_sample_size": 100,
    "performance_change_thresholds": null,
    "drift_statistic": "Population Stability Index",
    "params": {
      "min_num_quantiles": 1000,
      "distance_threshold": 0.2,
      "num_bins": 100
    },
    "ignore_nans": true
  },
  "prediction_drift": {
    "run": false,
    "drift_statistic": "Population Stability Index",
    "params": {
      "run": true,
      "min_sample_size": 100,
      "min_num_quantiles": 1000,
      "psi_thresholds": [
        0.2,
        0.4,
        0.6
      ],
      "num_bins": 100
    }
  },
  "embedding_drift": {
    "run": false,
    "min_sample_size": 100,
    "performance_change_thresholds": null,
    "drift_statistic": "euclidean_distance",
    "params": {
      "distance_threshold": 0.1,
      "normalize": true
    }
  },
  "avg_confidence": {
    "run": true,
    "severity_thresholds": [
      0.05,
      0.1,
      0.2
    ]
  },
  "atc": {
    "run": true,
    "severity_thresholds": [
      0.05,
      0.1,
      0.2
    ]
  },
  "calibration_comparison": {
    "run": true,
    "num_bins": 10,
    "severity_level_thresholds": [
      0.02,
      0.06,
      0.1
    ]
  },
  "label_imbalance": {
    "run": false,
    "severity_thresholds": [
      0.6,
      0.75,
      0.9
    ],
    "normalize": true
  },
  "global_sample_size": null,
  "metadata_tests": null,
  "global_target_text_keys": null,
  "unseen_unigram_abnormal_input": {
    "run": false,
    "severity_thresholds": [
      0.0,
      0.0002,
      0.0005
    ],
    "performance_impact_config": {
      "ignore_observed_performance": false,
      "min_num_samples": 1,
      "severity_thresholds": [
        0.01,
        0.05,
        0.1
      ]
    },
    "p_value_threshold": 0.0005
  },
  "empty_string_abnormal_input": {
    "run": false,
    "severity_thresholds": [
      0.0,
      0.0002,
      0.0005
    ],
    "performance_impact_config": {
      "ignore_observed_performance": false,
      "min_num_samples": 1,
      "severity_thresholds": [
        0.01,
        0.05,
        0.1
      ]
    }
  },
  "char_dist_drift": {
    "run": false,
    "drift_metrics": [
      {
        "distance_metric": "Population Stability Index",
        "severity_threshold": [
          0.1,
          0.2,
          0.4
        ]
      }
    ],
    "min_occurrences": 0,
    "model_impact_config": {
      "ignore_observed_performance": false,
      "min_num_samples": 1,
      "severity_thresholds": [
        0.01,
        0.05,
        0.1
      ]
    }
  },
  "unigrams_drift": {
    "run": false,
    "drift_metrics": [
      {
        "distance_metric": "Population Stability Index",
        "severity_threshold": [
          0.1,
          0.2,
          0.4
        ]
      }
    ],
    "min_occurrences": 5,
    "model_impact_config": {
      "ignore_observed_performance": false,
      "min_num_samples": 1,
      "severity_thresholds": [
        0.01,
        0.05,
        0.1
      ]
    }
  },
  "bigrams_drift": {
    "run": false,
    "drift_metrics": [
      {
        "distance_metric": "Population Stability Index",
        "severity_threshold": [
          0.1,
          0.2,
          0.4
        ]
      }
    ],
    "min_occurrences": 5,
    "model_impact_config": {
      "ignore_observed_performance": false,
      "min_num_samples": 1,
      "severity_thresholds": [
        0.01,
        0.05,
        0.1
      ]
    }
  },
  "lower_case_entity": {
    "run": true,
    "sample_size": 200,
    "severity_thresholds": [
      0,
      0.1,
      0.3
    ]
  },
  "upper_case_entity": {
    "run": true,
    "sample_size": 200,
    "severity_thresholds": [
      0,
      0.1,
      0.3
    ]
  },
  "ampersand": {
    "run": true,
    "sample_size": 200,
    "severity_thresholds": [
      0,
      0.1,
      0.3
    ]
  },
  "abbreviation": {
    "run": true,
    "sample_size": 200,
    "severity_thresholds": [
      0,
      0.1,
      0.3
    ]
  },
  "white_space_special_chars": {
    "run": true,
    "sample_size": 200,
    "severity_thresholds": [
      0,
      0.1,
      0.3
    ]
  },
  "ascii": {
    "run": true,
    "sample_size": 200,
    "severity_thresholds": [
      0,
      0.1,
      0.3
    ]
  },
  "remove_special_chars": {
    "run": true,
    "sample_size": 200,
    "severity_thresholds": [
      0,
      0.1,
      0.3
    ]
  },
  "swap_seen_entities": {
    "run": true,
    "sample_size": 200,
    "severity_thresholds": [
      0,
      0.1,
      0.3
    ]
  },
  "swap_unseen_entities": {
    "run": true,
    "sample_size": 200,
    "severity_thresholds": [
      0,
      0.1,
      0.3
    ]
  },
  "ground_truth_entity_type": {
    "run": true,
    "metric_name": "Recall",
    "num_subsets": 5,
    "min_subset_size": 10,
    "severity_thresholds": [
      0.05,
      0.08,
      0.13
    ]
  },
  "predicted_entity_type": {
    "run": true,
    "metric_name": "Precision",
    "num_subsets": 5,
    "min_subset_size": 10,
    "severity_thresholds": [
      0.05,
      0.08,
      0.13
    ]
  },
  "entity_types_drift": {
    "run": false,
    "drift_metrics": [
      {
        "distance_metric": "Population Stability Index",
        "severity_threshold": [
          0.1,
          0.2,
          0.4
        ]
      }
    ],
    "min_occurrences": 0,
    "model_impact_config": {
      "ignore_observed_performance": false,
      "min_num_samples": 1,
      "severity_thresholds": [
        0.01,
        0.05,
        0.1
      ]
    }
  },
  "predicted_entity_types_drift": {
    "run": false,
    "drift_metrics": [
      {
        "distance_metric": "Population Stability Index",
        "severity_threshold": [
          0.1,
          0.2,
          0.4
        ]
      }
    ],
    "min_occurrences": 0,
    "model_impact_config": {
      "ignore_observed_performance": false,
      "min_num_samples": 1,
      "severity_thresholds": [
        0.01,
        0.05,
        0.1
      ]
    }
  },
  "entity_lengths_drift": {
    "run": false,
    "drift_metrics": [
      {
        "distance_metric": "Population Stability Index",
        "severity_threshold": [
          0.1,
          0.2,
          0.4
        ]
      }
    ],
    "min_occurrences": 0,
    "model_impact_config": {
      "ignore_observed_performance": false,
      "min_num_samples": 1,
      "severity_thresholds": [
        0.01,
        0.05,
        0.1
      ]
    },
    "num_quantiles": 1001,
    "num_bins": 100
  }
}
```