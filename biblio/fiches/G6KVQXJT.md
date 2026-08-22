# VAST (Volume Annotation and Segmentation Tool): Efficient Manual and Semi-Automatic Labeling of Large 3D Image Stacks

**Auteurs** : Daniel R. Berger, H. Sebastian Seung, Jeff W. Lichtman
**Année** : 2018
**DOI** : 10.3389/fncir.2018.00088

## Résumé

Recent developments in serial-section electron microscopy allow the efficient generation of very large image data sets but analyzing such data poses challenges for software tools. Here we introduce Volume Annotation and Segmentation Tool (VAST), a freely available utility program for generating and editing annotations and segmentations of large volumetric image (voxel) data sets. It provides a simple yet powerful user interface for real-time exploration and analysis of large data sets even in the Petabyte range.

## Conclusions

Extraction failed: LLM call failed after trying 5 provider(s) with 3 retries each. Last error: LLM error: 503

## Available data and file formats for importing and exporting in Volume Annotation and Segmentation Tool (VAST) and VastTools. store arbitrary subregions of a large data set and to make arbitrary extension of those regions possible as users continue to trace, a tree of file-internal pointer blocks (16 × 16 × 16 pointers per block/tree node) is maintained which references the storage location of different segmentation image blocks within the segmentation file. Pointer blocks are also cached in memory when the segmentation file is opened in VAST for optimal file access speed. Selective storage of subregions of the dataset keeps file sizes small if sparse segmentations are generated on very large image stacks.

| Importing | To | Data formats | File formats |
| --- | --- | --- | --- |
| Exporting | To | Data formats | File formats |
|  | Segmentation metadata | Text file | .txt |
| VastTools.m | 3D object meshes | Triangle mesh | .obj/.mtl |
|  | Isosurface shells | Triangle mesh | .obj/.mtl |
|  | 3D particle clouds | Triangle mesh | .obj/.mtl |
|  | 3D scale bars | Triangle mesh | .obj/.mtl |
|  | Surface measurements | Text file | .txt |
|  | Volume measurements | Text file | .txt |
|  | Particle metadata | Text file | .txt |
