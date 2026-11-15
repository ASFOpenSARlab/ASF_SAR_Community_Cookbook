# ASF SAR Community Cookbook

<img src="assets/ASF_logo.svg" alt="thumbnail" width="300"/>

[![nightly-build](https://github.com/ASFOpenSARlab/ASF_Cookbook_Template/actions/workflows/nightly-build.yaml/badge.svg)](https://github.com/ASFOpenSARlab/ASF_Cookbook_Template/actions/workflows/nightly-build.yaml)

## Motivation

The SAR Community Cookbook is an open, collaborative resource for the Synthetic Aperture Radar (SAR) community to share knowledge and develop workflows.

This cookbook brings together community-contributed examples of SAR processing techniques, algorithms, and analysis pipelines. It provides a platform for researchers to share their approaches, build upon existing work, and improve methods through community collaboration and feedback.

## Community Contributions and Feedback

The workflows in this cookbook are community-contributed and have not been formally vetted or validated. While contributed code is expected to execute successfully prior to inclusion, no guarantees are made regarding the scientific correctness, accuracy, or suitability of methods or results. Users should critically evaluate workflows before applying them to their own research or applications.

Community participation is central to this project. We encourage users to share feedback, report problems, suggest improvements, and discuss approaches through GitHub Issues and Discussions.

## Code of Conduct

Our [Code of Conduct](https://github.com/ASFOpenSARlab/ASF_SAR_Community_Cookbook/blob/main/CODE_OF_CONDUCT.md) outlines expectations for respectful, inclusive, and constructive participation to foster a welcoming and collaborative community.

### Contributors

<a href="https://github.com/ASFOpenSARlab/ASF_Cookbook_Template/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=ASFOpenSARlab/ASF_Cookbook_Template" />
</a>

## Structure

This cookbook begins with a "General SAR" chapter, and is then broken up by mission.

1. ### General SAR
1. ### NISAR
1. ### Sentinel-1


## Running the Notebooks

### Running in a Jupyter Hub

If you are working in a Jupyter Hub that allows you to build Pixi environments, such as [OpenSARLab](https://opensarlab-docs.asf.alaska.edu/user-guides/opensarlab/), use the following steps to run the notebooks in this cookbook.

1. Clone the repository:

   ```bash
    git clone https://github.com/ASFOpenSARlab/ASF_SAR_Community_Cookbook.git
   ```

1. Run the `notebooks/software_environment.ipynb` notebook.

### Running on Your Own Machine

If you are interested in running this material locally on your computer, you will need to follow this workflow:

1. Clone the new repository:

   ```bash
    git clone https://github.com/ASFOpenSARlab/ASF_SAR_Community_Cookbook.git
   ```

1. Move into the `ASF_SAR_Community_Cookbook` directory
   ```bash
   cd ASF_SAR_Community_Cookbook
   ```
1. Launch in Jupyter Lab with the included Pixi environment
    ```bash
    pix run lab
    ```
