### Text Classification Testing Config


Below is the default configuration for all Text Classification tests. A copy of this can also be found in your `rime_trial` bundle (inside the `nlp_examples/classification/default_test_config.json`).

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
    "bound_multiplier": 2.0
  },
  "unseen_categorical": {
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
      0.3
    ]
  },
  "categorical_label_drift": {
    "run": false,
    "drift_statistic": "Population Stability Index",
    "params": {
      "psi_thresholds": [
        0.2,
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
        0.6
      ],
      "num_bins": 100
    }
  },
  "feature_drift": {
    "exclude_columns": [],
    "run": false,
    "min_sample_size": 100,
    "performance_change_thresholds": null,
    "numeric_feature_params": {
      "drift_statistic": "Population Stability Index",
      "min_num_quantiles": 1000,
      "num_bins": 100,
      "psi_threshold": 0.2,
      "kl_divergence_threshold": 0.1,
      "js_divergence_threshold": 0.05,
      "ks_test_p_value_threshold": 0.05,
      "ks_test_min_sample_size": 100,
      "ignore_nans": true
    },
    "categorical_feature_params": {
      "drift_statistic": "Population Stability Index",
      "chi_squared_p_value_threshold": 0.05,
      "psi_threshold": 0.2,
      "max_sample_size": null,
      "ignore_nans": true
    }
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
      0.2
    ]
  },
  "atc": {
    "run": true,
    "severity_thresholds": [
      0.05,
      0.2
    ]
  },
  "calibration_comparison": {
    "run": true,
    "num_bins": 10,
    "severity_level_thresholds": [
      0.02,
      0.1
    ]
  },
  "label_imbalance": {
    "run": false,
    "severity_thresholds": [
      0.6,
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
      0.0005
    ],
    "performance_impact_config": {
      "ignore_observed_performance": false,
      "min_num_samples": 1,
      "severity_thresholds": [
        0.01,
        0.1
      ]
    },
    "p_value_threshold": 0.0005
  },
  "empty_string_abnormal_input": {
    "run": false,
    "severity_thresholds": [
      0.0,
      0.0005
    ],
    "performance_impact_config": {
      "ignore_observed_performance": false,
      "min_num_samples": 1,
      "severity_thresholds": [
        0.01,
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
        0.1
      ]
    }
  },
  "invisible_chars_attack": {
    "target_text_keys": null,
    "run": false,
    "sample_size": 5,
    "severity_thresholds": [
      0.1,
      0.5
    ],
    "attack_params": {
      "target_score": 0.0,
      "max_queries": 200,
      "population_size": 15,
      "max_unsuccessful_iters": 25,
      "max_consecutive_unsuccessful": 3
    },
    "mutation_params": {
      "aug_char_p": 0.01
    },
    "max_str_len": 2000
  },
  "deletion_chars_attack": {
    "target_text_keys": null,
    "run": false,
    "sample_size": 5,
    "severity_thresholds": [
      0.1,
      0.5
    ],
    "attack_params": {
      "target_score": 0.0,
      "max_queries": 200,
      "population_size": 15,
      "max_unsuccessful_iters": 25,
      "max_consecutive_unsuccessful": 3
    },
    "mutation_params": {
      "aug_char_p": 0.01
    },
    "max_str_len": 2000
  },
  "intentional_homoglyph_attack": {
    "target_text_keys": null,
    "run": false,
    "sample_size": 5,
    "severity_thresholds": [
      0.1,
      0.5
    ],
    "attack_params": {
      "target_score": 0.0,
      "max_queries": 200,
      "population_size": 15,
      "max_unsuccessful_iters": 25,
      "max_consecutive_unsuccessful": 3
    },
    "mutation_params": {
      "aug_char_p": 0.01
    },
    "max_str_len": 2000
  },
  "confusable_homoglyph_attack": {
    "target_text_keys": null,
    "run": false,
    "sample_size": 5,
    "severity_thresholds": [
      0.1,
      0.5
    ],
    "attack_params": {
      "target_score": 0.0,
      "max_queries": 200,
      "population_size": 15,
      "max_unsuccessful_iters": 25,
      "max_consecutive_unsuccessful": 3
    },
    "mutation_params": {
      "aug_char_p": 0.01
    },
    "max_str_len": 2000
  },
  "universal_triggers_attack": {
    "target_text_keys": null,
    "run": false,
    "sample_size": 3,
    "batch_size": 10,
    "severity_thresholds": [
      0.1,
      0.3
    ],
    "attack_params": {
      "target_score": 0.0,
      "max_queries": 500,
      "population_size": 2,
      "max_unsuccessful_iters": 200,
      "max_consecutive_unsuccessful": 10
    },
    "mutation_params": {
      "prefix_len": 10,
      "aug_word_p": 0.2
    }
  },
  "char_substitution_attack": {
    "target_text_keys": null,
    "run": true,
    "sample_size": 200,
    "severity_thresholds": [
      0.1,
      0.3
    ],
    "max_str_len": 2000,
    "attack_params": {
      "min_char": 2,
      "aug_char_max": 1,
      "aug_char_min": 1,
      "aug_char_p": 0.1,
      "aug_word_min": 1,
      "aug_word_max": null,
      "aug_word_p": 0.05
    }
  },
  "char_deletion_attack": {
    "target_text_keys": null,
    "run": true,
    "sample_size": 200,
    "severity_thresholds": [
      0.1,
      0.3
    ],
    "max_str_len": 2000,
    "attack_params": {
      "min_char": 2,
      "aug_char_max": 1,
      "aug_char_min": 1,
      "aug_char_p": 0.1,
      "aug_word_min": 1,
      "aug_word_max": null,
      "aug_word_p": 0.05
    }
  },
  "char_insertion_attack": {
    "target_text_keys": null,
    "run": true,
    "sample_size": 200,
    "severity_thresholds": [
      0.1,
      0.3
    ],
    "max_str_len": 2000,
    "attack_params": {
      "min_char": 2,
      "aug_char_max": 1,
      "aug_char_min": 1,
      "aug_char_p": 0.1,
      "aug_word_min": 1,
      "aug_word_max": null,
      "aug_word_p": 0.05
    }
  },
  "char_swap_attack": {
    "target_text_keys": null,
    "run": true,
    "sample_size": 200,
    "severity_thresholds": [
      0.1,
      0.3
    ],
    "max_str_len": 2000,
    "attack_params": {
      "min_char": 2,
      "aug_char_max": 1,
      "aug_char_min": 1,
      "aug_char_p": 0.1,
      "aug_word_min": 1,
      "aug_word_max": null,
      "aug_word_p": 0.05
    }
  },
  "keyboard_aug_attack": {
    "target_text_keys": null,
    "run": true,
    "sample_size": 200,
    "severity_thresholds": [
      0.1,
      0.3
    ],
    "max_str_len": 2000,
    "attack_params": {
      "min_char": 2,
      "aug_char_max": 1,
      "aug_char_min": 1,
      "aug_char_p": 0.1,
      "aug_word_min": 1,
      "aug_word_max": null,
      "aug_word_p": 0.05
    }
  },
  "common_misspelling_attack": {
    "target_text_keys": null,
    "run": true,
    "sample_size": 200,
    "severity_thresholds": [
      0.1,
      0.3
    ],
    "max_str_len": 2000,
    "attack_params": null
  },
  "ocr_error_attack": {
    "target_text_keys": null,
    "run": true,
    "sample_size": 200,
    "severity_thresholds": [
      0.1,
      0.3
    ],
    "max_str_len": 2000,
    "attack_params": null
  },
  "synonym_swap_attack": {
    "target_text_keys": null,
    "run": false,
    "sample_size": 200,
    "severity_thresholds": [
      0.1,
      0.3
    ],
    "max_str_len": 2000,
    "attack_params": null
  },
  "lm_word_substitution_attack": {
    "target_text_keys": null,
    "run": false,
    "sample_size": 200,
    "severity_thresholds": [
      0.1,
      0.3
    ],
    "max_str_len": 2000,
    "attack_params": {
      "aug_min": 1,
      "aug_max": null,
      "aug_p": 0.05,
      "model_path": "distilbert-base-cased"
    }
  },
  "lm_word_insertion_attack": {
    "target_text_keys": null,
    "run": false,
    "sample_size": 200,
    "severity_thresholds": [
      0.1,
      0.3
    ],
    "max_str_len": 2000,
    "attack_params": {
      "aug_min": 1,
      "aug_max": null,
      "aug_p": 0.05,
      "model_path": "distilbert-base-cased"
    }
  },
  "upper_case_text": {
    "target_text_keys": null,
    "run": true,
    "sample_size": 200,
    "severity_thresholds": [
      0.1,
      0.3
    ],
    "max_str_len": 2000
  },
  "lower_case_text": {
    "target_text_keys": null,
    "run": true,
    "sample_size": 200,
    "severity_thresholds": [
      0.1,
      0.3
    ],
    "max_str_len": 2000
  },
  "remove_special_chars": {
    "target_text_keys": null,
    "run": true,
    "sample_size": 200,
    "severity_thresholds": [
      0.1,
      0.3
    ],
    "max_str_len": 2000
  },
  "swap_masc_to_fem": {
    "target_text_keys": null,
    "run": false,
    "sample_size": 200,
    "severity_thresholds": [
      0.1,
      0.3
    ],
    "max_str_len": 2000
  },
  "swap_fem_to_masc": {
    "target_text_keys": null,
    "run": false,
    "sample_size": 200,
    "severity_thresholds": [
      0.1,
      0.3
    ],
    "max_str_len": 2000
  },
  "swap_fem_name_to_masc_name": {
    "target_text_keys": null,
    "run": false,
    "sample_size": 200,
    "severity_thresholds": [
      0.1,
      0.3
    ],
    "max_str_len": 2000,
    "source": null,
    "target": null,
    "case_invariant": true
  },
  "swap_masc_name_to_fem_name": {
    "target_text_keys": null,
    "run": false,
    "sample_size": 200,
    "severity_thresholds": [
      0.1,
      0.3
    ],
    "max_str_len": 2000,
    "source": null,
    "target": null,
    "case_invariant": true
  },
  "ascii": {
    "target_text_keys": null,
    "run": true,
    "sample_size": 200,
    "severity_thresholds": [
      0.1,
      0.3
    ],
    "max_str_len": 2000
  },
  "exact_match_label_flipping": {
    "run": false,
    "severity_thresholds": [
      0.0,
      0.005
    ]
  }
}
```