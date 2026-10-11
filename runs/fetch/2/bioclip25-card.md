---

license:
- mit
language:
- en
library_name: open_clip
model_name: "BioCLIP 2.5 Huge"
model_description: "Foundation model for biology organismal images. It is trained on an updated version of TreeOfLife-200M on the basis of a CLIP model (ViT-H/14) pre-trained on LAION-2B. BioCLIP 2.5 Huge yields state-of-the-art performance in recognizing various species and further improves the performance on broader biological visual tasks."
tags:
- biology
- CV
- images
- imageomics
- clip
- species-classification
- biological visual task
- multimodal
- animals
- plants
- fungi
- species
- taxonomy
- rare species
- endangered species
- evolutionary biology
- knowledge-guided
- zero-shot-image-classification
datasets:
- imageomics/TreeOfLife-200M
- GBIF
- bioscan-ml/BIOSCAN-5M
- EOL
- FathomNet

---

<!--
Image with caption (jpg or png):

![Figure #](

https://huggingface.co/imageomics/

<model-repo>/resolve/main/<filepath>)

---

**Figure #.**

[Image of <>](

https://huggingface.co/imageomics/

<model-repo>/raw/main/<filepath>) <caption description>.

---

- ->

---

<!--
Notes on styling:

To render LaTex in your README, wrap the code in `\\\\(` and `\\\\)`. Example: \\(\frac{1}{2}\\)

Escape underscores ("_") with a "\". Example: image\_RGB
-->

# Model Card for BioCLIP 2.5 Huge

BioCLIP 2.5 Huge is a foundation model for biology organismal images. It is trained on [TreeOfLife-200M](https://huggingface.co/datasets/imageomics/TreeOfLife-200M) on the basis of a [CLIP](https://huggingface.co/laion/CLIP-ViT-H-14-laion2B-s32B-b79K) model (ViT-H/14) pre-trained on LAION-2B.
BioCLIP 2.5 Huge yields state-of-the-art performance in recognizing various species and further improves the performance on broader biological visual tasks.

## Model Details

### Model Description

BioCLIP 2.5 Huge is trained on an updated version of [TreeOfLife-200M](https://huggingface.co/datasets/imageomics/TreeOfLife-200M) that adds 19M more images to the original version (dataset to be updated with new metadata and species embeddings). In addition to the slightly larger training dataset, BioCLIP 2.5 Huge was extended to a ViT-H/14 backbone, in comparison with the ViT-L/14 backbone adopted by BioCLIP 2. The training was based on an updated version of the [BioCLIP 2](https://github.com/Imageomics/bioclip-2) repository ([v2.0.0](https://github.com/Imageomics/bioclip-2/tree/v2.0.0)), where `torchcompile` and `pure_bf16` were used for acceleration. 

The model achieves new state-of-the-art performance on both species classification and broader biological visual tasks, surpassing BioCLIP 2 by 5.7% and 3.5%, respectively. Especially in FishNet, which requires the model to distinguish different habitats, BioCLIP 2.5 Huge demonstrates a 8.7% performance improvement over BioCLIP 2. 

- **Developed by:** Jianyang Gu, Samuel Stevens, Elizabeth G Campolongo, Matthew J Thompson, Net Zhang, Jiaman Wu, Andrei Kopanev, Zheda Mai, Alexander E. White, James Balhoff, Wasila M Dahdul, Daniel Rubenstein, Hilmar Lapp, Tanya Berger-Wolf, Wei-Lun Chao, and Yu Su
- **Model type:** The model uses a ViT-H/14 Transformer as an image encoder and uses a masked self-attention Transformer as a text encoder.
- **License:** MIT
- **Fine-tuned from model:** CLIP pre-trained on LAION-2B, ViT-H/14 ([Model weight](https://huggingface.co/laion/CLIP-ViT-H-14-laion2B-s32B-b79K))

### Model Sources

- **Homepage:** [BioCLIP 2 Project Page](https://imageomics.github.io/bioclip-2/)
- **Repository:** [BioCLIP 2](https://github.com/Imageomics/bioclip-2)
- **Paper:** [BioCLIP 2: Emergent Properties from Scaling Hierarchical Contrastive Learning](https://doi.org/10.48550/arXiv.2505.23883)

## Uses

BioCLIP 2.5 Huge provides improved performance over [BioCLIP 2](https://huggingface.co/imageomics/bioclip-2); however, it is a much larger model, with higher resource requirements for inference.

### Direct Use

The model can be used for zero-shot classification provided the taxonomic or vernacular names.
It can also be used for few-shot classification with some images serving as the support set.
Additionally, it is also recommended to use BioCLIP 2.5 Huge as a visual encoder for other biological visual tasks.

## Bias, Risks, and Limitations

Please refer to the discussion in the corresponding section of the [BioCLIP 2 model card](https://huggingface.co/imageomics/bioclip-2#bias-risks-and-limitations). 

<!--

### Recommendations

This section is meant to convey recommendations with respect to the bias, risk, and technical limitations.

Users (both direct and downstream) should be made aware of the risks, biases and limitations of the model. More information needed for further recommendations.
-->

## How to Get Started with the Model

You can use the `open_clip` library to load BioCLIP 2.5 Huge.

```python
import open_clip
model, preprocess_train, preprocess_val = open_clip.create_model_and_transforms('hf-hub:imageomics/bioclip-2.5-vith14')
tokenizer = open_clip.get_tokenizer('hf-hub:imageomics/bioclip-2.5-vith14')
```

## Training Details

### Training Data

The model was trained with an updated version of [TreeOfLife-200M](https://huggingface.co/datasets/imageomics/TreeOfLife-200M) which included an additional 19M images and some additional content-based filtering (details to be updated).

We used a subset of LAION-2B that consists of 26M samples for experience replay.
This part of data was downloaded from the first three parquet metadata files of LAION-2B, and the first 4,000 tar files were used. This is the same subset used in BioCLIP 2 training for experience replay.

### Training Procedure

### Preprocessing

Standard CLIP image preprocessing is adopted in the training.

### Training Hyperparameters

- **Training regime:** pure bf16 precision <!--fp32, fp16 mixed precision, bf16 mixed precision, bf16 non-mixed precision, fp16 non-mixed precision, fp8 mixed precision -->

As with [BioCLIP 2](https://huggingface.co/imageomics/bioclip-2#training-hyperparameters), we used an Adam optimizer with a maximum learning rate of 1e-4. For this larger model, 20,000 warming steps were adopted, followed by cosine decay; the batch size of biological images was 1,152 per GPU, and that of replay data was 128 per GPU. We trained the model on 32 GPUs for 25 epochs, with a weight decay of 0.2. Each input image was resized to 224 x 224 resolution.

## Evaluation

We evaluated the model on both species classification and other biological visual tasks. All the test data matches that used to evaluate [BioCLIP 2](https://huggingface.co/imageomics/bioclip-2#testing-data), though we repeat it here for ease of reference.

### Testing Data

For species classification tasks, we tested BioCLIP 2.5 Huge on the following 10 tasks:

- [NABirds](https://dl.allaboutbirds.org/nabirds): We used 555 visual categories of 48,640 images for test.
- [Meta-Album](https://meta-album.github.io/): We used the Plankton, Insects, Insects2, PlantNet, Fungi, PlantVillage, and Medicinal Leaf datasets from Meta-Album.
- [IDLE-OO Camera Traps](https://huggingface.co/datasets/imageomics/IDLE-OO-Camera-Traps): Species identification in camera trap images is a real-world scenario that BioCLIP 2 can be applied to.
We collected a class-balanced test set from five LILA-BC camera trap datasets. For more information on this test set, please visit the [dataset page](https://huggingface.co/datasets/imageomics/IDLE-OO-Camera-Traps).
- [Rare Species](https://huggingface.co/datasets/imageomics/rare-species): This dataset was introduced in the first BioCLIP paper.
It consists of 400 species labeled Near Threatened through Extinct in the Wild by the [IUCN Red List](https://www.iucnredlist.org/), with 30 images per species.
Top-1 accuracy is reported for both zero-shot and few-shot experiments.

For biological visual tasks beyond species classification, we used:

- [FishNet](https://fishnet-2023.github.io/): We used the original training set (75,631) images to train a two-layer linear classifier on top of the extracted features to predict the feeding path and habitat labels.
Then we tested the classifier with 18,901 images from the test set. Accuracy is reported as the metric, where only predicting all the 9 labels correctly counts as success.
- [NeWT](https://github.com/visipedia/newt): We used the 164 binary classification tasks proposed in the dataset. Micro-accuracy is reported across all the samples.
- [AwA2](https://cvml.ista.ac.at/AwA2/): We used the original train-test split for attribute classification. Macro-F1 score is reported across all the attributes.
- [Herbarium19](https://www.kaggle.com/c/herbarium-2019-fgvc6): This is task to discover new species. We implement it as semi-supervised clustering. Clustering accuracy is calculated for the predictions on both seen and unseen classes.
- [PlantDoc](https://github.com/pratikkayal/PlantDoc-Dataset): 2,598 images of 13 plant species and up to 17 classes of diseases are included in this dataset. We conducted the experiment in a multi-fold 1-shot learning fashion. Average accuracy over the test samples is reported.

More details regarding the evaluation implementation can be referred to in the [paper](https://doi.org/10.48550/arXiv.2505.23883).

### Results

We show the zero-shot classification and non-species classification task results here.
<table cellpadding="0" cellspacing="0">
<thead>
<tr>
<th rowspan="2">Model</th>
<th colspan="5">Animals</th>
<th colspan="4">Plants & Fungi</th>
<th rowspan="2">Rare Species</th>
<th rowspan="2">Mean</th>
</tr>
<tr>
<th>NABirds</th>
<th>Plankton</th>
<th>Insects</th>
<th>Insects 2</th>
<th>Camera Trap</th>
<th>PlantNet</th>
<th>Fungi</th>
<th>PlantVillage</th>
<th>Med. Leaf</th>
</tr>
</thead>
<tbody>
<tr>
<td>BioCLIP</td>
<td>58.8</td>
<td><b>6.1</b></td>
<td>34.9</td>
<td>20.5</td>
<td>31.7</td>
<td>88.2</td>
<td>40.9</td>
<td>19.0</td>
<td>38.5</td>
<td>37.1</td>
<td>37.6</td>
</tr>
<tr>
<td>BioCLIP 2</td>
<td>74.9</td>
<td>3.9</td>
<td>55.3</td>
<td>27.7</td>
<td>53.9</td>
<td>96.8</td>
<td>83.8</td>
<td>25.1</td>
<td>57.8</td>
<td>76.8</td>
<td>55.6</td>
</tr>
<tr>
<td>BioCLIP 2.5 Huge</td>
<td><b>75.8</b></td>
<td>5.2</td>
<td><b>68.2</b></td>
<td><b>30.8</b></td>
<td><b>58.7</b></td>
<td><b>96.9</b></td>
<td><b>84.9</b></td>
<td><b>33.5</b></td>
<td><b>73.2</b></td>
<td><b>85.5</b></td>
<td><b>61.3</b></td>
</tr>
</tbody>
</table>

<table cellpadding="0" cellspacing="0">
<thead>
<tr>
<th rowspan="2">Model</th>
<th colspan="3">Animals</th>
<th colspan="2">Plants</th>
<th rowspan="2">Mean</th>
</tr>
<tr>
<th>FishNet</th>
<th>NeWT</th>
<th>AwA2</th>
<th>Herbarium19</th>
<th>PlantDoc</th>
</tr>
</thead>
<tbody>
<tr>
<td>SigLIP 2</td>
<td>34.0</td>
<td>82.7</td>
<td>67.9</td>
<td>20.2</td>
<td>28.4</td>
<td>46.6</td>
</tr>
<tr>
<td>DINOv3</td>
<td>37.9</td>
<td>85.7</td>
<td>48.0</td>
<td>31.2</td>
<td>40.3</td>
<td>48.6</td>
</tr>
<tr>
<td>BioCLIP</td>
<td>30.1</td>
<td>82.7</td>
<td>65.9</td>
<td>26.8</td>
<td>39.5</td>
<td>49.0</td>
</tr>
<tr>
<td>BioCLIP 2</td>
<td>39.8</td>
<td>89.1</td>
<td>69.5</td>
<td>48.6</td>
<td>40.4</td>
<td>57.5</td>
</tr>
<tr>
<td>BioCLIP 2.5 Huge</td>
<td><b>48.5</b></td>
<td><b>90.0</b></td>
<td><b>72.9</b></td>
<td><b>51.9</b></td>
<td><b>41.9</b></td>
<td><b>61.0</b></td>
</tr>
</tbody>
</table>

### Summary

BioCLIP 2.5 Huge surpasses BioCLIP 2 by 5.7% on zero-shot species classification benchmarks and 3.5% on broader biological visual tasks.

## Technical Specifications

### Compute Infrastructure

As with [BioCLIP 2](https://huggingface.co/imageomics/bioclip-2#compute-infrastructure), the training was performed on 32 NVIDIA H100-80GB GPUs distributed over 4 nodes on [Pittsburgh Supercomputing Center](https://www.psc.edu/)'s Bridges-2 Cluster.
Though it took 11 days to complete the BioCLIP 2.5 Huge training of 25 epochs.

## Citation

**BibTeX:**

```
@software{Gu_BioCLIP_2.5_Huge_model,
  author = {Jianyang Gu and Samuel Stevens and Elizabeth G Campolongo and Matthew J Thompson and Net Zhang and Jiaman Wu and Andrei Kopanev and Zheda Mai and Alexander E. White and James Balhoff and Wasila M Dahdul and Daniel Rubenstein and Hilmar Lapp and Tanya Berger-Wolf and Wei-Lun Chao and Yu Su},
  license = {MIT},
  title = {{BioCLIP 2.5 Huge}},
  url = {https://huggingface.co/imageomics/bioclip-2.5-vith14},
  version = {1.0.0},
  doi = {10.57967/hf/10131},
  publisher = {Hugging Face},
  year = {2026}
}
```

Please also cite our paper:

```
@inproceedings{NEURIPS2025_94da80cb,
 author = {Gu, Jianyang and Stevens, Sam and Campolongo, Elizabeth and Thompson, Matthew and Zhang, Net and Wu, Jiaman and Kopanev, Andrei and Mai, Zheda and White, Alexander and Balhoff, James and Dahdul, Wasila and Rubenstein, Daniel and Lapp, Hilmar and Berger-Wolf, Tanya and Chao, Wei-Lun (Harry) and Su, Yu},
 booktitle = {Advances in Neural Information Processing Systems},
 editor = {D. Belgrave and C. Zhang and H. Lin and R. Pascanu and P. Koniusz and M. Ghassemi and N. Chen},
 pages = {102778--102811},
 publisher = {Curran Associates, Inc.},
 title = {BioCLIP 2: Emergent Properties from Scaling Hierarchical Contrastive Learning},
 url = {https://proceedings.neurips.cc/paper_files/paper/2025/file/94da80cbfe870c1db958c88a8a27018c-Paper-Conference.pdf},
 volume = {38},
 year = {2025},
 doi = {10.52202/085713-3436}
}
```

Also consider citing OpenCLIP and BioCLIP:

```
@software{ilharco_gabriel_2021_5143773,
  author={Ilharco, Gabriel and Wortsman, Mitchell and Wightman, Ross and Gordon, Cade and Carlini, Nicholas and Taori, Rohan and Dave, Achal and Shankar, Vaishaal and Namkoong, Hongseok and Miller, John and Hajishirzi, Hannaneh and Farhadi, Ali and Schmidt, Ludwig},
  title={OpenCLIP},
  year={2021},
  doi={10.5281/zenodo.5143773},
}
```

Original BioCLIP Model:

```
@software{bioclip2023,
  author = {Samuel Stevens and Jiaman Wu and Matthew J. Thompson and Elizabeth G. Campolongo and Chan Hee Song and David Edward Carlyn and Li Dong and Wasila M. Dahdul and Charles Stewart and Tanya Berger-Wolf and Wei-Lun Chao and Yu Su},
  doi = {10.57967/hf/1511},
  month = nov,
  title = {BioCLIP},
  version = {v0.1},
  year = {2023}
}
```

Original BioCLIP Paper:

```
@inproceedings{stevens2024bioclip,
  title = {{B}io{CLIP}: A Vision Foundation Model for the Tree of Life},
  author = {Samuel Stevens and Jiaman Wu and Matthew J Thompson and Elizabeth G Campolongo and Chan Hee Song and David Edward Carlyn and Li Dong and Wasila M Dahdul and Charles Stewart and Tanya Berger-Wolf and Wei-Lun Chao and Yu Su},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
  year = {2024},
  pages = {19412-19424}
}
```

## Acknowledgements

We would like to thank Zhiyuan Tao, Shuheng Wang, Ziheng Zhang, Zhongwei Wang, and Leanna House for their help with the TreeOfLife-200M dataset, Charles (Chuck) Stewart, Sara Beery, and other [Imageomics Team](https://imageomics.osu.edu/about/team) members for their constructive feedback and Sergiu Sanielevici, Tom Maiden, and TJ Olesky for their dedicated assistance with arranging the necessary computational resources.

We are grateful to Kakani Katija and Dirk Steinke for helpful conversations regarding use and integration of FathomNet and BIOSCAN-5M, respectively, as well as Stephen Formel and Markus Döring for GBIF. We thank Marie Grosjean for comparative methods for filtering citizen science images and Dylan Verheul for assistance with acquiring images from [Observation.org](http://observation.org/) from GBIF. We thank Suren Byna for a helpful conversation on early dataset design decisions. We thank Doug Johnson for his collaboration in hosting this large dataset on the Ohio Supercomputer Center research storage file system.

This work was supported by the [Imageomics Institute](https://imageomics.org/), which is funded by the US National Science Foundation's Harnessing the Data Revolution (HDR) program under [Award #2118240](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2118240) (Imageomics: A New Frontier of Biological Information Powered by Knowledge-Guided Machine Learning).

Our research is also supported by resources from the [Ohio Supercomputer Center](https://ror.org/01apna436). This work used the [Bridges-2](https://doi.org/10.1145/3437359.3465593) system, which is supported by NSF award number OAC-1928147 at the Pittsburgh Supercomputing Center (PSC), under the auspices of the [NAIRR Pilot program](https://nairrpilot.org/).

Any opinions, findings and conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the National Science Foundation.

<!-- ## Glossary  -->

<!-- [optional] If relevant, include terms and calculations in this section that can help readers understand the model or model card. -->

<!-- ## More Information  -->

<!-- [optional] Any other relevant information that doesn't fit elsewhere. -->

## Model Card Authors

Jianyang Gu

## Model Card Contact

[gu.1220@osu.edu](mailto:gu.1220@osu.edu)