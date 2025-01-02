# Cell-Type-Plot/ tSNE Plot

This script generates a scatter plot visualizing cell types (monocyte, bCell, tCell) based on their positions in a tSNE space. The script reads two input TSV files:
1. `position.tsv`: Contains cell barcodes and tSNE coordinates.
2. `celltype.tsv`: Maps cell barcodes to their respective cell types.

The output is a PNG file of the tSNE plot, with cells colored by type and labeled with the median positions for each cell type.

## Requirements
- Python 3.x
- Libraries: `matplotlib`, `numpy`, `argparse`

## Usage
```bash
python BME163_tSNE_Plot.py -p <position.tsv> -c <celltype.tsv> -o <output.png>
