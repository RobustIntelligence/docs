### Text Classification Testing Config


Below is the default configuration for all Text Classification tests. A copy of this can also be found in your `rime_trial` bundle (inside the `nlp_examples/classification/default_test_config.json`).

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
  "invisible_chars_attack": {
    "run": true,
    "sample_size": 5,
    "target_text_keys": null,
    "severity_thresholds": [
      0.1,
      0.25,
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
    "run": true,
    "sample_size": 5,
    "target_text_keys": null,
    "severity_thresholds": [
      0.1,
      0.25,
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
    "run": true,
    "sample_size": 5,
    "target_text_keys": null,
    "severity_thresholds": [
      0.1,
      0.25,
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
    "run": true,
    "sample_size": 5,
    "target_text_keys": null,
    "severity_thresholds": [
      0.1,
      0.25,
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
    "run": true,
    "sample_size": 3,
    "target_text_keys": null,
    "batch_size": 10,
    "severity_thresholds": [
      0.1,
      0.2,
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
    "run": true,
    "sample_size": 200,
    "target_text_keys": null,
    "severity_thresholds": [
      0.1,
      0.2,
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
    "run": true,
    "sample_size": 200,
    "target_text_keys": null,
    "severity_thresholds": [
      0.1,
      0.2,
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
    "run": true,
    "sample_size": 200,
    "target_text_keys": null,
    "severity_thresholds": [
      0.1,
      0.2,
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
    "run": true,
    "sample_size": 200,
    "target_text_keys": null,
    "severity_thresholds": [
      0.1,
      0.2,
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
    "run": true,
    "sample_size": 200,
    "target_text_keys": null,
    "severity_thresholds": [
      0.1,
      0.2,
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
    "run": true,
    "sample_size": 200,
    "target_text_keys": null,
    "severity_thresholds": [
      0.1,
      0.2,
      0.3
    ],
    "max_str_len": 2000,
    "attack_params": null
  },
  "ocr_error_attack": {
    "run": true,
    "sample_size": 200,
    "target_text_keys": null,
    "severity_thresholds": [
      0.1,
      0.2,
      0.3
    ],
    "max_str_len": 2000,
    "attack_params": null
  },
  "synonym_swap_attack": {
    "run": true,
    "sample_size": 200,
    "target_text_keys": null,
    "severity_thresholds": [
      0.1,
      0.2,
      0.3
    ],
    "max_str_len": 2000,
    "attack_params": {
      "aug_min": 1,
      "aug_max": null,
      "aug_p": 0.05
    }
  },
  "lm_word_substitution_attack": {
    "run": true,
    "sample_size": 200,
    "target_text_keys": null,
    "severity_thresholds": [
      0.1,
      0.2,
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
    "run": true,
    "sample_size": 200,
    "target_text_keys": null,
    "severity_thresholds": [
      0.1,
      0.2,
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
    "run": true,
    "sample_size": 200,
    "target_text_keys": null,
    "severity_thresholds": [
      0.1,
      0.2,
      0.3
    ],
    "max_str_len": 2000
  },
  "lower_case_text": {
    "run": true,
    "sample_size": 200,
    "target_text_keys": null,
    "severity_thresholds": [
      0.1,
      0.2,
      0.3
    ],
    "max_str_len": 2000
  },
  "remove_special_chars": {
    "run": true,
    "sample_size": 200,
    "target_text_keys": null,
    "severity_thresholds": [
      0.1,
      0.2,
      0.3
    ],
    "max_str_len": 2000
  },
  "swap_masc_to_fem": {
    "run": true,
    "sample_size": 200,
    "target_text_keys": null,
    "severity_thresholds": [
      0.1,
      0.2,
      0.3
    ],
    "max_str_len": 2000
  },
  "swap_fem_to_masc": {
    "run": true,
    "sample_size": 200,
    "target_text_keys": null,
    "severity_thresholds": [
      0.1,
      0.2,
      0.3
    ],
    "max_str_len": 2000
  },
  "swap_fem_name_to_masc_name": {
    "run": true,
    "sample_size": 200,
    "target_text_keys": null,
    "severity_thresholds": [
      0.1,
      0.2,
      0.3
    ],
    "max_str_len": 2000,
    "source": null,
    "target": null,
    "case_invariant": true
  },
  "swap_masc_name_to_fem_name": {
    "run": true,
    "sample_size": 200,
    "target_text_keys": null,
    "severity_thresholds": [
      0.1,
      0.2,
      0.3
    ],
    "max_str_len": 2000,
    "source": null,
    "target": null,
    "case_invariant": true
  },
  "ascii": {
    "run": true,
    "sample_size": 200,
    "target_text_keys": null,
    "severity_thresholds": [
      0.1,
      0.2,
      0.3
    ],
    "max_str_len": 2000
  }
}
```
