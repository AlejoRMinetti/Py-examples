/*
 * Copyright (c) 2013, The WebRTC project authors. All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are
 * met:
 *
 *   * Redistributions of source code must retain the above copyright
 *     notice, this list of conditions and the following disclaimer.
 *
 *   * Redistributions in binary form must reproduce the above copyright
 *     notice, this list of conditions and the following disclaimer in
 *     the documentation and/or other materials provided with the
 *     distribution.
 *
 *   * Neither the name of Google nor the names of its contributors may
 *     be used to endorse or promote products derived from this software
 *     without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 * "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 * LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
 * A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
 * HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
 * SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
 * LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
 * DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
 * THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
 * OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

#ifndef AVCODEC_ILBCDATA_H
#define AVCODEC_ILBCDATA_H

#include "libavutil/common.h"

static const uint8_t lsf_dim_codebook[] = { 3, 3, 4 };
static const uint8_t lsf_size_codebook[] = { 64, 128, 128 };
static const int16_t lsf_weight_20ms[] = { 12288, 8192, 4096, 0 };
static const int16_t lsf_weight_30ms[] = { 8192, 16384, 10923, 5461, 0, 0 };

static const int16_t hp_out_coeffs[] = { 3849, -7699, 3849, 7918, -3833 };

static const int16_t kPlcPfSlope[] = { 26667, 18729, 13653, 10258, 7901, 6214 };

static const int16_t kPlcPitchFact[] = { 0, 5462, 10922, 16384, 21846, 27306 };

static const int16_t kCbFiltersRev[] = {
    -140, 446, -755, 3302, 2922, -590, 343, -138
};

static const int16_t kPlcPerSqr[] = { 839, 1343, 2048, 2998, 4247, 5849 };

static const int16_t alpha[] = {
    6554, 13107, 19661, 26214
};

static const int16_t kLpcChirpSyntDenum[] = {
    32767, 29573, 26690, 24087, 21739, 19619, 17707, 15980, 14422, 13016, 11747
};

static const int16_t LpcChirpWeightDenum[] = {
    32767, 13835, 5841, 2466, 1041, 440, 186, 78,  33,  14,  6
};

static const int16_t cos_tbl[64] = {
    32767,  32729,  32610,  32413,  32138,  31786,  31357,   30853,
    30274,  29622,  28899,  28106,  27246,  26320,  25330,   24279,
    23170,  22006,  20788,  19520,  18205,  16846,  15447,   14010,
    12540,  11039,   9512,   7962,   6393,   4808,   3212,    1608,
    0,      -1608,  -3212,  -4808,  -6393,  -7962,  -9512,  -11039,
    -12540, -14010, -15447, -16846, -18205, -19520, -20788, -22006,
    -23170, -24279, -25330, -26320, -27246, -28106, -28899, -29622,
    -30274, -30853, -31357, -31786, -32138, -32413, -32610, -32729,
};

static const int16_t cos_derivative_tbl[64] = {
    -632,  -1893,  -3150,  -4399,  -5638,  -6863,  -8072,  -9261,
    -10428, -11570, -12684, -13767, -14817, -15832, -16808, -17744,
    -18637, -19486, -20287, -21039, -21741, -22390, -22986, -23526,
    -24009, -24435, -24801, -25108, -25354, -25540, -25664, -25726,
    -25726, -25664, -25540, -25354, -25108, -24801, -24435, -24009,
    -23526, -22986, -22390, -21741, -21039, -20287, -19486, -18637,
    -17744, -16808, -15832, -14817, -13767, -12684, -11570, -10428,
    -9261,  -8072,  -6863,  -5638,  -4399,  -3150,  -1893,   -632
};

static const int16_t lsf_codebook[64 * 3 + 128 * 3 + 128 * 4] = {
    1273, 2238, 3696, 3199, 5309, 8209, 3606, 5671, 7829,
    2815, 5262, 8778, 2608, 4027, 5493, 1582, 3076, 5945,
    2983, 4181, 5396, 2437, 4322, 6902, 1861, 2998, 4613,
    2007, 3250, 5214, 1388, 2459, 4262, 2563, 3805, 5269,
    2036, 3522, 5129, 1935, 4025, 6694, 2744, 5121, 7338,
    2810, 4248, 5723, 3054, 5405, 7745, 1449, 2593, 4763,
    3411, 5128, 6596, 2484, 4659, 7496, 1668, 2879, 4818,
    1812, 3072, 5036, 1638, 2649, 3900, 2464, 3550, 4644,
    1853, 2900, 4158, 2458, 4163, 5830, 2556, 4036, 6254,
    2703, 4432, 6519, 3062, 4953, 7609, 1725, 3703, 6187,
    2221, 3877, 5427, 2339, 3579, 5197, 2021, 4633, 7037,
    2216, 3328, 4535, 2961, 4739, 6667, 2807, 3955, 5099,
    2788, 4501, 6088, 1642, 2755, 4431, 3341, 5282, 7333,
    2414, 3726, 5727, 1582, 2822, 5269, 2259, 3447, 4905,
    3117, 4986, 7054, 1825, 3491, 5542, 3338, 5736, 8627,
    1789, 3090, 5488, 2566, 3720, 4923, 2846, 4682, 7161,
    1950, 3321, 5976, 1834, 3383, 6734, 3238, 4769, 6094,
    2031, 3978, 5903, 1877, 4068, 7436, 2131, 4644, 8296,
    2764, 5010, 8013, 2194, 3667, 6302, 2053, 3127, 4342,
    3523, 6595, 10010, 3134, 4457, 5748, 3142, 5819, 9414,
    2223, 4334, 6353, 2022, 3224, 4822, 2186, 3458, 5544,
    2552, 4757, 6870, 10905, 12917, 14578, 9503, 11485, 14485,
    9518, 12494, 14052, 6222, 7487, 9174, 7759, 9186, 10506,
    8315, 12755, 14786, 9609, 11486, 13866, 8909, 12077, 13643,
    7369, 9054, 11520, 9408, 12163, 14715, 6436, 9911, 12843,
    7109, 9556, 11884, 7557, 10075, 11640, 6482, 9202, 11547,
    6463, 7914, 10980, 8611, 10427, 12752, 7101, 9676, 12606,
    7428, 11252, 13172, 10197, 12955, 15842, 7487, 10955, 12613,
    5575, 7858, 13621, 7268, 11719, 14752, 7476, 11744, 13795,
    7049, 8686, 11922, 8234, 11314, 13983, 6560, 11173, 14984,
    6405, 9211, 12337, 8222, 12054, 13801, 8039, 10728, 13255,
    10066, 12733, 14389, 6016, 7338, 10040, 6896, 8648, 10234,
    7538, 9170, 12175, 7327, 12608, 14983, 10516, 12643, 15223,
    5538, 7644, 12213, 6728, 12221, 14253, 7563, 9377, 12948,
    8661, 11023, 13401, 7280, 8806, 11085, 7723, 9793, 12333,
    12225, 14648, 16709, 8768, 13389, 15245, 10267, 12197, 13812,
    5301, 7078, 11484, 7100, 10280, 11906, 8716, 12555, 14183,
    9567, 12464, 15434, 7832, 12305, 14300, 7608, 10556, 12121,
    8913, 11311, 12868, 7414, 9722, 11239, 8666, 11641, 13250,
    9079, 10752, 12300, 8024, 11608, 13306, 10453, 13607, 16449,
    8135, 9573, 10909, 6375, 7741, 10125, 10025, 12217, 14874,
    6985, 11063, 14109, 9296, 13051, 14642, 8613, 10975, 12542,
    6583, 10414, 13534, 6191, 9368, 13430, 5742, 6859, 9260,
    7723, 9813, 13679, 8137, 11291, 12833, 6562, 8973, 10641,
    6062, 8462, 11335, 6928, 8784, 12647, 7501, 8784, 10031,
    8372, 10045, 12135, 8191, 9864, 12746, 5917, 7487, 10979,
    5516, 6848, 10318, 6819, 9899, 11421, 7882, 12912, 15670,
    9558, 11230, 12753, 7752, 9327, 11472, 8479, 9980, 11358,
    11418, 14072, 16386, 7968, 10330, 14423, 8423, 10555, 12162,
    6337, 10306, 14391, 8850, 10879, 14276, 6750, 11885, 15710,
    7037, 8328, 9764, 6914, 9266, 13476, 9746, 13949, 15519,
    11032, 14444, 16925, 8032, 10271, 11810, 10962, 13451, 15833,
    10021, 11667, 13324, 6273, 8226, 12936, 8543, 10397, 13496,
    7936, 10302, 12745, 6769, 8138, 10446, 6081, 7786, 11719,
    8637, 11795, 14975, 8790, 10336, 11812, 7040, 8490, 10771,
    7338, 10381, 13153, 6598, 7888, 9358, 6518, 8237, 12030,
    9055, 10763, 12983, 6490, 10009, 12007, 9589, 12023, 13632,
    6867, 9447, 10995, 7930, 9816, 11397, 10241, 13300, 14939,
    5830, 8670, 12387, 9870, 11915, 14247, 9318, 11647, 13272,
    6721, 10836, 12929, 6543, 8233, 9944, 8034, 10854, 12394,
    9112, 11787, 14218, 9302, 11114, 13400, 9022, 11366, 13816,
    6962, 10461, 12480, 11288, 13333, 15222, 7249, 8974, 10547,
    10566, 12336, 14390, 6697, 11339, 13521, 11851, 13944, 15826,
    6847, 8381, 11349, 7509, 9331, 10939, 8029, 9618, 11909,
    13973, 17644, 19647, 22474, 14722, 16522, 20035, 22134, 16305, 18179, 21106, 23048,
    15150, 17948, 21394, 23225, 13582, 15191, 17687, 22333, 11778, 15546, 18458, 21753,
    16619, 18410, 20827, 23559, 14229, 15746, 17907, 22474, 12465, 15327, 20700, 22831,
    15085, 16799, 20182, 23410, 13026, 16935, 19890, 22892, 14310, 16854, 19007, 22944,
    14210, 15897, 18891, 23154, 14633, 18059, 20132, 22899, 15246, 17781, 19780, 22640,
    16396, 18904, 20912, 23035, 14618, 17401, 19510, 21672, 15473, 17497, 19813, 23439,
    18851, 20736, 22323, 23864, 15055, 16804, 18530, 20916, 16490, 18196, 19990, 21939,
    11711, 15223, 21154, 23312, 13294, 15546, 19393, 21472, 12956, 16060, 20610, 22417,
    11628, 15843, 19617, 22501, 14106, 16872, 19839, 22689, 15655, 18192, 20161, 22452,
    12953, 15244, 20619, 23549, 15322, 17193, 19926, 21762, 16873, 18676, 20444, 22359,
    14874, 17871, 20083, 21959, 11534, 14486, 19194, 21857, 17766, 19617, 21338, 23178,
    13404, 15284, 19080, 23136, 15392, 17527, 19470, 21953, 14462, 16153, 17985, 21192,
    17734, 19750, 21903, 23783, 16973, 19096, 21675, 23815, 16597, 18936, 21257, 23461,
    15966, 17865, 20602, 22920, 15416, 17456, 20301, 22972, 18335, 20093, 21732, 23497,
    15548, 17217, 20679, 23594, 15208, 16995, 20816, 22870, 13890, 18015, 20531, 22468,
    13211, 15377, 19951, 22388, 12852, 14635, 17978, 22680, 16002, 17732, 20373, 23544,
    11373, 14134, 19534, 22707, 17329, 19151, 21241, 23462, 15612, 17296, 19362, 22850,
    15422, 19104, 21285, 23164, 13792, 17111, 19349, 21370, 15352, 17876, 20776, 22667,
    15253, 16961, 18921, 22123, 14108, 17264, 20294, 23246, 15785, 17897, 20010, 21822,
    17399, 19147, 20915, 22753, 13010, 15659, 18127, 20840, 16826, 19422, 22218, 24084,
    18108, 20641, 22695, 24237, 18018, 20273, 22268, 23920, 16057, 17821, 21365, 23665,
    16005, 17901, 19892, 23016, 13232, 16683, 21107, 23221, 13280, 16615, 19915, 21829,
    14950, 18575, 20599, 22511, 16337, 18261, 20277, 23216, 14306, 16477, 21203, 23158,
    12803, 17498, 20248, 22014, 14327, 17068, 20160, 22006, 14402, 17461, 21599, 23688,
    16968, 18834, 20896, 23055, 15070, 17157, 20451, 22315, 15419, 17107, 21601, 23946,
    16039, 17639, 19533, 21424, 16326, 19261, 21745, 23673, 16489, 18534, 21658, 23782,
    16594, 18471, 20549, 22807, 18973, 21212, 22890, 24278, 14264, 18674, 21123, 23071,
    15117, 16841, 19239, 23118, 13762, 15782, 20478, 23230, 14111, 15949, 20058, 22354,
    14990, 16738, 21139, 23492, 13735, 16971, 19026, 22158, 14676, 17314, 20232, 22807,
    16196, 18146, 20459, 22339, 14747, 17258, 19315, 22437, 14973, 17778, 20692, 23367,
    15715, 17472, 20385, 22349, 15702, 18228, 20829, 23410, 14428, 16188, 20541, 23630,
    16824, 19394, 21365, 23246, 13069, 16392, 18900, 21121, 12047, 16640, 19463, 21689,
    14757, 17433, 19659, 23125, 15185, 16930, 19900, 22540, 16026, 17725, 19618, 22399,
    16086, 18643, 21179, 23472, 15462, 17248, 19102, 21196, 17368, 20016, 22396, 24096,
    12340, 14475, 19665, 23362, 13636, 16229, 19462, 22728, 14096, 16211, 19591, 21635,
    12152, 14867, 19943, 22301, 14492, 17503, 21002, 22728, 14834, 16788, 19447, 21411,
    14650, 16433, 19326, 22308, 14624, 16328, 19659, 23204, 13888, 16572, 20665, 22488,
    12977, 16102, 18841, 22246, 15523, 18431, 21757, 23738, 14095, 16349, 18837, 20947,
    13266, 17809, 21088, 22839, 15427, 18190, 20270, 23143, 11859, 16753, 20935, 22486,
    12310, 17667, 21736, 23319, 14021, 15926, 18702, 22002, 12286, 15299, 19178, 21126,
    15703, 17491, 21039, 23151, 12272, 14018, 18213, 22570, 14817, 16364, 18485, 22598,
    17109, 19683, 21851, 23677, 12657, 14903, 19039, 22061, 14713, 16487, 20527, 22814,
    14635, 16726, 18763, 21715, 15878, 18550, 20718, 22906
};

static const int16_t gain3[9]={
    -16384, -10813, -5407, 0, 4096, 8192, 12288, 16384, 32767
};

static const int16_t gain4[17]={
    -17203, -14746, -12288, -9830, -7373, -4915, -2458, 0, 2458, 4915, 7373, 9830,
    12288, 14746, 17203, 19661, 32767
};

static const int16_t gain5[33]={
    614,   1229,  1843,  2458,  3072,  3686,
    4301,  4915,  5530,  6144,  6758,  7373,
    7987,  8602,  9216,  9830,  10445, 11059,
    11674, 12288, 12902, 13517, 14131, 14746,
    15360, 15974, 16589, 17203, 17818, 18432,
    19046, 19661, 32767
};

static const int16_t *const ilbc_gain[] = {
    gain5, gain4, gain3,
};

static const int16_t ilbc_state[8] = {
   -30473, -17838, -9257, -2537, 3639, 10893, 19958, 32636
};

static const int16_t frg_quant_mod[64] = {
    /* First 37 values in Q8 */
    569, 671, 786, 916, 1077, 1278,
    1529, 1802, 2109, 2481, 2898, 3440,
    3943, 4535, 5149, 5778, 6464, 7208,
    7904, 8682, 9397, 10285, 11240, 12246,
    13313, 14382, 15492, 16735, 18131, 19693,
    21280, 22912, 24624, 26544, 28432, 30488,
    32720,
    /* 22 values in Q5 */
    4383, 4684, 5012, 5363, 5739, 6146,
    6603, 7113, 7679, 8285, 9040, 9850,
    10838, 11882, 13103, 14467, 15950, 17669,
    19712, 22016, 24800, 28576,
    /* 5 values in Q3 */
    8240, 9792, 12040, 15440, 22472
};

#endif /* AVCODEC_ILBCDATA_H */
