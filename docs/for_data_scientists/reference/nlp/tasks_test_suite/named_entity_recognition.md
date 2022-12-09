### Named Entity Recognition Testing Config


Below is the default configuration for all Named Entity Recognition tests. A copy of this can also be found in your `rime_trial` bundle (inside the `nlp_examples/ner/default_test_config.json`).

```python
{
  "categories": [],
  "run_default": null,
  "custom_tests": null,
  "numeric_outlier": {
    "exclude_columns": [],
    "run": true,
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
    "run": true,
    "performance_change_config": {
      "severity_thresholds": null,
      "min_num_samples": 1
    }
  },
  "unseen_domain": {
    "exclude_columns": [],
    "run": true,
    "performance_change_config": {
      "severity_thresholds": null,
      "min_num_samples": 1
    }
  },
  "unseen_email": {
    "exclude_columns": [],
    "run": true,
    "performance_change_config": {
      "severity_thresholds": null,
      "min_num_samples": 1
    }
  },
  "unseen_url": {
    "exclude_columns": [],
    "run": true,
    "performance_change_config": {
      "severity_thresholds": null,
      "min_num_samples": 1
    }
  },
  "rare_categories": {
    "exclude_columns": [],
    "run": true,
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
    "run": true,
    "performance_change_config": {
      "severity_thresholds": null,
      "min_num_samples": 1
    }
  },
  "inconsistencies": {
    "exclude_columns": [],
    "run": true,
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
    "run": true,
    "performance_change_config": {
      "severity_thresholds": null,
      "min_num_samples": 1
    }
  },
  "empty_string": {
    "exclude_columns": [],
    "run": true,
    "performance_change_config": {
      "severity_thresholds": null,
      "min_num_samples": 1
    }
  },
  "embedding_anomalies": {
    "exclude_columns": [],
    "run": true,
    "performance_change_config": {
      "severity_thresholds": null,
      "min_num_samples": 10
    },
    "distance_quantile": 0.995
  },
  "feat_subset_auc": {
    "exclude_columns": [],
    "run": true,
    "min_sample_size": 20,
    "performance_change_thresholds": null
  },
  "feat_subset_accuracy": {
    "exclude_columns": [],
    "run": true,
    "min_sample_size": 20,
    "performance_change_thresholds": null
  },
  "feat_subset_f1": {
    "exclude_columns": [],
    "run": true,
    "min_sample_size": 20,
    "performance_change_thresholds": null
  },
  "feat_subset_macro_f1": {
    "exclude_columns": [],
    "run": true,
    "min_sample_size": 20,
    "performance_change_thresholds": null
  },
  "feat_subset_precision": {
    "exclude_columns": [],
    "run": true,
    "min_sample_size": 20,
    "performance_change_thresholds": null
  },
  "feat_subset_macro_precision": {
    "exclude_columns": [],
    "run": true,
    "min_sample_size": 20,
    "performance_change_thresholds": null
  },
  "feat_subset_fpr": {
    "exclude_columns": [],
    "run": true,
    "min_sample_size": 20,
    "performance_change_thresholds": null
  },
  "feat_subset_recall": {
    "exclude_columns": [],
    "run": true,
    "min_sample_size": 20,
    "performance_change_thresholds": null
  },
  "feat_subset_macro_recall": {
    "exclude_columns": [],
    "run": true,
    "min_sample_size": 20,
    "performance_change_thresholds": null
  },
  "feat_subset_pred_variance_pos": {
    "exclude_columns": [],
    "run": true,
    "min_sample_size": 20,
    "performance_change_thresholds": null
  },
  "feat_subset_pred_variance_neg": {
    "exclude_columns": [],
    "run": true,
    "min_sample_size": 20,
    "performance_change_thresholds": null
  },
  "feat_subset_rmse": {
    "exclude_columns": [],
    "run": true,
    "min_sample_size": 20,
    "performance_change_thresholds": null
  },
  "feat_subset_mae": {
    "exclude_columns": [],
    "run": true,
    "min_sample_size": 20,
    "performance_change_thresholds": null
  },
  "feat_subset_mape": {
    "exclude_columns": [],
    "run": true,
    "min_sample_size": 20,
    "performance_change_thresholds": null
  },
  "feat_subset_rank_correlation": {
    "exclude_columns": [],
    "run": true,
    "min_sample_size": 20,
    "performance_change_thresholds": null
  },
  "feat_subset_ndcg": {
    "exclude_columns": [],
    "run": true,
    "min_sample_size": 20,
    "performance_change_thresholds": null
  },
  "feat_subset_mrr": {
    "exclude_columns": [],
    "run": true,
    "min_sample_size": 20,
    "performance_change_thresholds": null
  },
  "feat_subset_multiclass_acc": {
    "exclude_columns": [],
    "run": true,
    "min_sample_size": 20,
    "performance_change_thresholds": null
  },
  "feat_subset_multiclass_auc": {
    "exclude_columns": [],
    "run": true,
    "min_sample_size": 20,
    "performance_change_thresholds": null
  },
  "feat_subset_drift_auc": {
    "exclude_columns": [],
    "run": true,
    "min_sample_size": 20,
    "performance_change_thresholds": null
  },
  "feat_subset_drift_accuracy": {
    "exclude_columns": [],
    "run": true,
    "min_sample_size": 20,
    "performance_change_thresholds": null
  },
  "feat_subset_drift_f1": {
    "exclude_columns": [],
    "run": true,
    "min_sample_size": 20,
    "performance_change_thresholds": null
  },
  "feat_subset_drift_macro_f1": {
    "exclude_columns": [],
    "run": true,
    "min_sample_size": 20,
    "performance_change_thresholds": null
  },
  "feat_subset_drift_precision": {
    "exclude_columns": [],
    "run": true,
    "min_sample_size": 20,
    "performance_change_thresholds": null
  },
  "feat_subset_drift_macro_precision": {
    "exclude_columns": [],
    "run": true,
    "min_sample_size": 20,
    "performance_change_thresholds": null
  },
  "feat_subset_drift_fpr": {
    "exclude_columns": [],
    "run": true,
    "min_sample_size": 20,
    "performance_change_thresholds": null
  },
  "feat_subset_drift_recall": {
    "exclude_columns": [],
    "run": true,
    "min_sample_size": 20,
    "performance_change_thresholds": null
  },
  "feat_subset_drift_macro_recall": {
    "exclude_columns": [],
    "run": true,
    "min_sample_size": 20,
    "performance_change_thresholds": null
  },
  "feat_subset_drift_pred_variance_pos": {
    "exclude_columns": [],
    "run": true,
    "min_sample_size": 20,
    "performance_change_thresholds": null
  },
  "feat_subset_drift_pred_variance_neg": {
    "exclude_columns": [],
    "run": true,
    "min_sample_size": 20,
    "performance_change_thresholds": null
  },
  "feat_subset_drift_pred_variance_all": {
    "exclude_columns": [],
    "run": true,
    "min_sample_size": 20,
    "performance_change_thresholds": null
  },
  "feat_subset_drift_rmse": {
    "exclude_columns": [],
    "run": true,
    "min_sample_size": 20,
    "performance_change_thresholds": null
  },
  "feat_subset_drift_mae": {
    "exclude_columns": [],
    "run": true,
    "min_sample_size": 20,
    "performance_change_thresholds": null
  },
  "feat_subset_drift_mape": {
    "exclude_columns": [],
    "run": true,
    "min_sample_size": 20,
    "performance_change_thresholds": null
  },
  "feat_subset_drift_rank_correlation": {
    "exclude_columns": [],
    "run": true,
    "min_sample_size": 20,
    "performance_change_thresholds": null
  },
  "feat_subset_drift_ndcg": {
    "exclude_columns": [],
    "run": true,
    "min_sample_size": 20,
    "performance_change_thresholds": null
  },
  "feat_subset_drift_mrr": {
    "exclude_columns": [],
    "run": true,
    "min_sample_size": 20,
    "performance_change_thresholds": null
  },
  "feat_subset_drift_multiclass_acc": {
    "exclude_columns": [],
    "run": true,
    "min_sample_size": 20,
    "performance_change_thresholds": null
  },
  "feat_subset_drift_multiclass_auc": {
    "exclude_columns": [],
    "run": true,
    "min_sample_size": 20,
    "performance_change_thresholds": null
  },
  "correlation_feat_drift": {
    "exclude_columns": [],
    "run": true,
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
    "run": true,
    "correlation_drift_thresholds": [
      0.3,
      0.5,
      0.7
    ],
    "p_value_threshold": 0.05
  },
  "mutual_information_feat_drift": {
    "exclude_columns": [],
    "run": true,
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
    "run": true,
    "mutual_information_thresholds": [
      0.1,
      0.2,
      0.3
    ]
  },
  "categorical_label_drift": {
    "run": true,
    "drift_statistic": "Population Stability Index",
    "params": {
      "run": true,
      "distance_thresholds": [
        0.2,
        0.4,
        0.6
      ]
    }
  },
  "multiclass_pred_label_drift": {
    "run": true,
    "drift_statistic": "Population Stability Index",
    "params": {
      "run": true,
      "distance_thresholds": [
        0.2,
        0.4,
        0.6
      ]
    }
  },
  "regression_label_drift": {
    "run": true,
    "p_value_threshold": 0.05,
    "ks_stat_thresholds": [
      0.1,
      0.33,
      0.67
    ]
  },
  "categorical_drift": {
    "exclude_columns": [],
    "run": true,
    "drift_scaling_factor": 0.005,
    "performance_change_thresholds": null,
    "drift_statistic": "Population Stability Index",
    "params": {
      "run": true,
      "drift_scaling_factor": 0.005,
      "performance_change_thresholds": null,
      "min_sample_size": 100,
      "max_sample_size": null,
      "distance_threshold": 0.2
    },
    "ignore_nans": true
  },
  "continuous_drift": {
    "exclude_columns": [],
    "run": true,
    "drift_scaling_factor": 0.005,
    "performance_change_thresholds": null,
    "drift_statistic": "Population Stability Index",
    "params": {
      "run": true,
      "drift_scaling_factor": 0.005,
      "performance_change_thresholds": null,
      "min_sample_size": 100,
      "min_num_quantiles": 1000,
      "distance_threshold": 0.2,
      "num_bins": 100
    },
    "ignore_nans": true
  },
  "prediction_drift": {
    "run": true,
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
    "exclude_columns": [],
    "run": true,
    "drift_scaling_factor": 0.005,
    "performance_change_thresholds": null,
    "drift_statistic": "euclidean_distance",
    "params": {
      "run": true,
      "drift_scaling_factor": 0.005,
      "performance_change_thresholds": null,
      "min_sample_size": 100,
      "distance_threshold": 0.1,
      "normalize": true
    }
  },
  "overall_metrics": {
    "run": true,
    "metrics_specific_thresholds": {}
  },
  "avg_confidence": {
    "run": true,
    "severity_thresholds": [
      0.03,
      0.08,
      0.13
    ]
  },
  "atc": {
    "run": true,
    "severity_thresholds": [
      0.03,
      0.08,
      0.13
    ]
  },
  "calibration_comparison": {
    "run": true,
    "severity_level_thresholds": [
      0.02,
      0.06,
      0.1
    ]
  },
  "label_imbalance": {
    "run": true,
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
    "run": true,
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
    "run": true,
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
    "run": true,
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
    "run": true,
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
    "run": true,
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
  "subset_precision": {
    "exclude_columns": [],
    "run": true,
    "min_sample_size": 20,
    "performance_change_thresholds": null
  },
  "subset_recall": {
    "exclude_columns": [],
    "run": true,
    "min_sample_size": 20,
    "performance_change_thresholds": null
  },
  "entity_types_drift": {
    "run": true,
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
    "run": true,
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
    "run": true,
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
