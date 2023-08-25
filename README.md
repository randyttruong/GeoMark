# GDPTrace 
## Introduction 
Geomark aims to improve upon current state-of-the-art privacy preserving techniques through a combination of local differential privacy, geo-indistinguishability, and data synthesis. Geomark is a reimplmentation of the trajectory synthesis mechanism defined in the paper 

> Yuntao Du, Yujia Hu, Zhikun Zhang, Ziquan Fang, Lu Chen, Baihua Zheng and Yunjun Gao (2023). LDPTrace: Locally Differentially Private Trajectory Synthesis. Paper in arXiv or PVLDB. In VLDB'23, Vancouver, Canada, August 28 to September 1, 2023.

in which I alter the original data perturbation method, Optimized Unary Encodings, to geo-indstinguishable differential privacy, whose implementation I derived from the paper

> Geo-Indistinguishability: Differential Privacy for Location-Based Systems.
M. Andres, N. Bordenabe, K. Chatzikokolakis and C. Palamidessi.
Proc. of CCS '13, ACM, pp. 901-914, 2013. 

## Abstract

Trajectory data is vital to fulfilling the promises of modern location-based services and applications. The growing importance and use-cases of trajectory data in these modern technologies, how- ever, has put into question the increasing threat of security and privacy vulnerabilities. In order to mediate these security concerns, state-of-the-art location-based services have implemented several privacy frameworks in order to preserve user-privacy within trajectory datasets and thereby make locational data feasible to implement in real-world applications. A proposed solution, geo-indistinguishability, provides a rigorous mathematical definition to how privacy should be distributed amongst geo-spatial data. A geo- indistinguishable framework of privacy, combined with another privacy solution, local differential privacy, requires that users share obfuscated versions of their data with data curators. This ensures that no external parties have access to a users’ personal information, but rather, only the most vital statistical aspects of their data. In this paper, a novel privacy framework based on LDPTrace, GeoMark is proposed in order to improve on the current privacy-utility compromise in state-of-the-art privacy-preserving techniques utilizing geo-indistinguishability.
