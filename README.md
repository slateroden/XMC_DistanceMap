# XMC_DistanceMap

XMC Red Clump Distance Map of the Magellanic Clouds

This repository provides the Red Clump (RC) distance map of the Magellanic Clouds derived Gaia DR3 photometry, as presented in:

Oden, S. J., et al. 2025, "Warped & Hooked: Mapping the Magellanic Clouds in 3D using Red Clump Stars", arXiv:2512.04200, doi:10.48550/arXiv.2512.04200

The map traces the three-dimensional structure of the Magellanic Clouds using RC stars as standard candles.

## Data Product:
MC_RC_Distance_Map_Oden25_galactic.fits

### Description:
  - Angular resolution: 15 arcminutes (0.25 deg)
  - Units: Distance in kiloparsecs (kpc)
  - Coordinate system: Galactic

Derived from RC stellar population modeling with local completeness and population corrections.

This map represents the final, peer-reviewed version of the distance product used in the associated manuscript.


## Usage Example

An example Python script demonstrating how to query the distance map is provided in:

query.py

## Reproducibility

All scripts in this repository were used to generate or validate the distance map presented in the paper. The archived Zenodo release corresponds exactly to the tagged GitHub release associated with the manuscript.

## Citation

If you use this dataset, please cite:

Oden, S. J., et al. 2025, "Warped & Hooked: Mapping the Magellanic Clouds in 3D using Red Clump Stars", arXiv:2512.04200, doi:10.48550/arXiv.2512.04200

and the Zenodo DOI for this repository:

DOI: 10.5281/zenodo.18330355

## License

This repository is released under the MIT License.

## Contact

For questions or issues, please contact:

Slater Oden
Montana State University
slateroden@montana.edu
