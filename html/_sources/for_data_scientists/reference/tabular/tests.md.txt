Tests Configuration
===================

All of the tests RIME runs are easily configurable via a JSON configuration file.
In order to use this configuration for a run, you should specify the path to this JSON
file in the overall configuration file using the `"tests_config_path"` key.

## Global Configuration Options

This JSON file contains several global configuration options, which, if specified, will apply to all relevant tests. All of these default to `null`, which means RIME will rely on the specific test configuration to provide this value. These are:

- **`categories`**: List[str], *default* = ``[]``

    Test categories to run. Options include `Abnormal Inputs`, `Attacks`, `Bias and Fairness`, `Data Cleanliness`, `Data Poisoning Detection`, `Drift`, `Model Performance`, `Subset Performance`, and `Transformations`.

- **`run_default`**: Optional[bool], *default* = ``null``

    Whether to run default categories or not. Defaults to `True` if no `categories` are specified, `False` if any are. The default categories are `Attacks`, `Model Performance`, `Subset Performance`, and `Transformations`.
- **`global_exclude_columns`**: Optional[List[str]], *default* = `null`

    Columns to exclude from all tests.
- **`global_abnormal_inputs_performance_change_config`**: Optional[mapping], *default* = `null`

    Parameters for measuring the impact of abnormal inputs on model performance (applies to all abnormal input tests). The different values of this mapping should be:
    - `severity_thresholds`: List[float, float]
      
      Ascending list of three float thresholds, corresponding to the observed or simulated performance change which must be achieved in order for the test to return, respectively, Low, Medium, or High severity. This is a logical OR: if both types of performance change are measured, take the maximum of the two and return the severity corresponding to the highest threshold that was exceeded. If there are observed failing rows but the observed or simulated performance changes do not exceed any of the thresholds, return a Low severity.
    - `min_num_samples`: int 
  
      The minimum number of rows needed to reliably compute performance change. If there are fewer than this many abnormal inputs, the observed model performance change will not be taken into when determining test status and severity.

- **`global_transformation_performance_change_config`**: Optional[mapping], *default* = `null`

    Parameters for measuring the impact of transformation on model performance (applies to all transformation tests). The different values of this mapping should be:
    - `severity_thresholds`: List[float, float]

      Ascending list of three float thresholds, corresponding to the observed or simulated performance change which must be achieved in order for the test to return, respectively, Low, Medium, or High severity. This is a logical OR: if both types of performance change are measured, take the maximum of the two and return the severity corresponding to the highest threshold that was exceeded. If there are observed failing rows but the observed or simulated performance changes do not exceed any of the thresholds, return a Low severity.
    - `ignore_errors`: bool
    
      If False, if the model raises an error on inputs with the given abnormality then the test case will fail with High severity.
    - `num_samples_to_simulate`: int 
  
      The number of clean rows to sample and perturb for the sake of measuring the simulated performance change.

- **`global_drift_scaling_factor`**: float

    Used for drift tests. How large of an estimated change in predictions is needed to increase the Model Impact Level by 1. Defaults to `0.005`.

Besides these global parameters, there are also keys for configuration for individual tests.

## Default configuration

Below is the default configuration for all tests. A copy of this can also be found in your `rime_trial` bundle (inside the `examples/test_configs/default_test_config.json`).

```json
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
  "global_exclude_columns": null,
  "global_abnormal_inputs_performance_change_config": null,
  "global_transformation_performance_change_config": null,
  "out_of_range_substitution": {
    "exclude_columns": [],
    "run": false,
    "performance_change_config": {
      "ignore_errors": false,
      "severity_thresholds": null,
      "num_samples_to_simulate": 100
    },
    "std_factor": 3
  },
  "outlier_substitution": {
    "exclude_columns": [],
    "run": true,
    "performance_change_config": {
      "ignore_errors": false,
      "severity_thresholds": null,
      "num_samples_to_simulate": 100
    },
    "bound_multiplier": 2.0
  },
  "feature_type_change": {
    "exclude_columns": [],
    "run": true,
    "performance_change_config": {
      "ignore_errors": false,
      "severity_thresholds": null,
      "num_samples_to_simulate": 100
    }
  },
  "empty_string_substitution": {
    "exclude_columns": [],
    "run": true,
    "performance_change_config": {
      "ignore_errors": false,
      "severity_thresholds": null,
      "num_samples_to_simulate": 100
    }
  },
  "req_characters_deletion": {
    "column_specific_params": {},
    "exclude_columns": [],
    "run": true,
    "performance_change_config": {
      "ignore_errors": false,
      "severity_thresholds": null,
      "num_samples_to_simulate": 100
    }
  },
  "unseen_categorical_substitution": {
    "exclude_columns": [],
    "run": true,
    "performance_change_config": {
      "ignore_errors": false,
      "severity_thresholds": null,
      "num_samples_to_simulate": 100
    }
  },
  "null_substitution": {
    "exclude_columns": [],
    "run": true,
    "performance_change_config": {
      "ignore_errors": false,
      "severity_thresholds": null,
      "num_samples_to_simulate": 100
    }
  },
  "capitalization_change": {
    "exclude_columns": [],
    "run": true,
    "performance_change_config": {
      "ignore_errors": false,
      "severity_thresholds": null,
      "num_samples_to_simulate": 100
    }
  },
  "text_upper_case": {
    "run": true,
    "sample_size": 20,
    "severity_thresholds": [
      0.1,
      0.3
    ],
    "max_str_len": 2000
  },
  "text_lower_case": {
    "run": true,
    "sample_size": 20,
    "severity_thresholds": [
      0.1,
      0.3
    ],
    "max_str_len": 2000
  },
  "text_remove_special_chars": {
    "run": true,
    "sample_size": 20,
    "severity_thresholds": [
      0.1,
      0.3
    ],
    "max_str_len": 2000
  },
  "text_ascii": {
    "run": true,
    "sample_size": 20,
    "severity_thresholds": [
      0.1,
      0.3
    ],
    "max_str_len": 2000
  },
  "text_char_substitution_attack": {
    "run": true,
    "sample_size": 20,
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
  "text_char_deletion_attack": {
    "run": true,
    "sample_size": 20,
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
  "text_char_insertion_attack": {
    "run": true,
    "sample_size": 20,
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
  "text_char_swap_attack": {
    "run": true,
    "sample_size": 20,
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
  "text_keyboard_aug_attack": {
    "run": true,
    "sample_size": 20,
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
  "text_common_misspelling_attack": {
    "run": true,
    "sample_size": 20,
    "severity_thresholds": [
      0.1,
      0.3
    ],
    "max_str_len": 2000,
    "attack_params": null
  },
  "text_ocr_error_attack": {
    "run": true,
    "sample_size": 20,
    "severity_thresholds": [
      0.1,
      0.3
    ],
    "max_str_len": 2000,
    "attack_params": null
  },
  "gaussian_blur": {
    "run": true,
    "sample_size": 50,
    "severity_thresholds": [
      0.1,
      0.3
    ],
    "kernel_size": [
      19,
      19
    ],
    "sigma": 5
  },
  "color_jitter": {
    "run": true,
    "sample_size": 50,
    "severity_thresholds": [
      0.1,
      0.3
    ],
    "brightness": 0.1,
    "contrast": 0.1,
    "saturation": 0.1,
    "hue": 0.1
  },
  "gaussian_noise": {
    "run": true,
    "sample_size": 50,
    "severity_thresholds": [
      0.01,
      0.25
    ],
    "mean": 0,
    "sigma": 0.03
  },
  "vertical_flip": {
    "run": true,
    "sample_size": 50,
    "severity_thresholds": [
      0.1,
      0.3
    ]
  },
  "horizontal_flip": {
    "run": true,
    "sample_size": 50,
    "severity_thresholds": [
      0.1,
      0.3
    ]
  },
  "randomize_pixels_with_mask": {
    "run": true,
    "sample_size": 50,
    "severity_thresholds": [
      0.1,
      0.3
    ],
    "probability": 0.1
  },
  "contrast_increase": {
    "run": true,
    "sample_size": 50,
    "severity_thresholds": [
      0.1,
      0.3
    ],
    "percent": 0.5
  },
  "contrast_decrease": {
    "run": true,
    "sample_size": 50,
    "severity_thresholds": [
      0.1,
      0.3
    ],
    "percent": 0.5
  },
  "add_rain": {
    "run": false,
    "sample_size": 50,
    "severity_thresholds": [
      0.1,
      0.3
    ],
    "alpha": 0.5
  },
  "add_snow": {
    "run": false,
    "sample_size": 50,
    "severity_thresholds": [
      0.1,
      0.3
    ],
    "alpha": 0.5
  },
  "vulnerability": {
    "exclude_columns": [],
    "run": false,
    "severity_level_thresholds": null,
    "sample_size": 10,
    "search_count": 10
  },
  "sensitivity": {
    "exclude_columns": [],
    "run": true,
    "severity_level_thresholds": null,
    "linf_constraint": 0.01,
    "sample_size": 10
  },
  "multi_feat_vulnerability": {
    "exclude_columns": [],
    "run": false,
    "severity_level_thresholds": null,
    "l0_constraint": 3,
    "sample_size": 10,
    "search_count": 10
  },
  "multi_feat_sensitivity": {
    "exclude_columns": [],
    "run": true,
    "severity_level_thresholds": null,
    "l0_constraint": 3,
    "sample_size": 10,
    "linf_constraint": 0.01
  },
  "hopskipjump_attack": {
    "exclude_columns": [],
    "run": false,
    "severity_thresholds": [
      0.05,
      0.25
    ],
    "sample_size": 10,
    "attack_params": {
      "targeted": false,
      "norm": 2,
      "max_iter": 50,
      "max_eval": 1000,
      "init_eval": 100,
      "init_size": 100
    }
  },
  "text_invisible_chars_attack": {
    "run": true,
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
  "text_deletion_chars_attack": {
    "run": true,
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
  "text_intentional_homoglyph_attack": {
    "run": true,
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
  "text_confusable_homoglyph_attack": {
    "run": true,
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
  "feature_type_check": {
    "exclude_columns": [],
    "run": false,
    "performance_change_config": {
      "severity_thresholds": null,
      "min_num_samples": 1
    }
  },
  "null_check": {
    "exclude_columns": [],
    "run": false,
    "performance_change_config": {
      "severity_thresholds": null,
      "min_num_samples": 1
    }
  },
  "null_proportion": {
    "exclude_columns": [],
    "run": false,
    "min_sample_size": 100,
    "performance_change_thresholds": null,
    "p_value_threshold": 0.05
  },
  "row_null_proportion": {
    "exclude_columns": [],
    "run": false,
    "min_sample_size": 100,
    "performance_change_thresholds": null,
    "drift_statistic": "Population Stability Index",
    "params": {
      "psi_threshold": 0.2
    }
  },
  "required_features": {
    "run": false,
    "required_feats": null,
    "allowed_feats": null,
    "ordered": false,
    "required_only": false
  },
  "duplicate_rows": {
    "exclude_columns": [],
    "run": false
  },
  "mi_decrease_feature_to_label": {
    "exclude_columns": [],
    "run": false,
    "severity_thresholds": [
      0.1,
      0.3
    ],
    "min_mutual_information_requirement": 0.2
  },
  "high_mi_feature_to_label": {
    "exclude_columns": [],
    "run": false,
    "severity_thresholds": [
      0.7,
      0.9
    ]
  },
  "high_feature_correlation": {
    "exclude_columns": [],
    "run": false,
    "severity_thresholds": [
      0.7,
      0.9
    ],
    "max_pairwise_tests": 200,
    "min_num_samples": 100
  },
  "protected_feature_drift": {
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
  "protected_proxies": {
    "exclude_columns": [],
    "run": false,
    "severity_thresholds": [
      0.2,
      0.4
    ]
  },
  "class_imbalance": {
    "exclude_columns": [],
    "run": false,
    "min_sample_size": 20,
    "performance_change_thresholds": [
      0.9,
      0.96
    ]
  },
  "equalized_odds": {
    "exclude_columns": [],
    "run": false,
    "min_sample_size": 20,
    "performance_change_thresholds": [
      0.1,
      0.3
    ]
  },
  "intersectional_group_fairness": {
    "exclude_columns": [],
    "run": false,
    "min_sample_size": 20,
    "performance_change_thresholds": null
  },
  "group_fairness_avg_pred": {
    "exclude_columns": [],
    "run": false,
    "min_sample_size": 20,
    "performance_change_thresholds": null
  },
  "group_fairness_avg_rank": {
    "exclude_columns": [],
    "run": false,
    "min_sample_size": 20,
    "performance_change_thresholds": null
  },
  "demographic_parity": {
    "exclude_columns": [],
    "run": false,
    "min_sample_size": 20,
    "performance_change_thresholds": [
      0.8,
      0.6
    ]
  },
  "demographic_parity_avg_pred": {
    "exclude_columns": [],
    "run": false,
    "min_sample_size": 20,
    "performance_change_thresholds": [
      0.8,
      0.6
    ]
  },
  "demographic_parity_avg_rank": {
    "exclude_columns": [],
    "run": false,
    "min_sample_size": 20,
    "performance_change_thresholds": [
      0.8,
      0.6
    ]
  },
  "chi_squared_independence": {
    "run": false,
    "p_value_thresholds": [
      0.005,
      0.05
    ],
    "min_sample_size": 100,
    "min_subset_sample_size": 20
  },
  "predict_protected_features": {
    "run": false,
    "accuracy_thresholds": [
      0.8,
      0.9
    ],
    "min_sample_size": 100,
    "non_protected_train_features": null,
    "max_protected_feature_cardinality": 100,
    "max_categorical_train_feature_cardinality": 100,
    "ref_data_split": 0.8
  },
  "subset_sensitivity_pos_pred": {
    "exclude_columns": [],
    "run": false,
    "performance_thresholds": [
      0.1,
      0.3
    ],
    "min_sample_size": 20,
    "num_samples_to_simulate": 100
  },
  "subset_sensitivity_avg_pred": {
    "exclude_columns": [],
    "run": false,
    "performance_thresholds": [
      0.1,
      0.3
    ],
    "min_sample_size": 20,
    "num_samples_to_simulate": 100
  },
  "subset_sensitivity_avg_rank": {
    "exclude_columns": [],
    "run": false,
    "performance_thresholds": [
      0.1,
      0.3
    ],
    "min_sample_size": 20,
    "num_samples_to_simulate": 100
  },
  "equal_opportunity": {
    "exclude_columns": [],
    "run": false,
    "min_sample_size": 20,
    "performance_change_thresholds": null
  },
  "equal_opp_macro_recall": {
    "exclude_columns": [],
    "run": false,
    "min_sample_size": 20,
    "performance_change_thresholds": null
  },
  "predictive_equality": {
    "exclude_columns": [],
    "run": false,
    "min_sample_size": 20,
    "performance_change_thresholds": null
  },
  "exact_match_label_flipping": {
    "exclude_columns": [],
    "run": false,
    "severity_thresholds": [
      0.0,
      0.005
    ]
  }
}
```