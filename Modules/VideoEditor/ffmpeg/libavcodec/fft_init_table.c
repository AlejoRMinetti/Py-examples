/*
 * Copyright (c) 2012
 *      MIPS Technologies, Inc., California.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 * 1. Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 * 2. Redistributions in binary form must reproduce the above copyright
 *    notice, this list of conditions and the following disclaimer in the
 *    documentation and/or other materials provided with the distribution.
 * 3. Neither the name of the MIPS Technologies, Inc., nor the names of its
 *    contributors may be used to endorse or promote products derived from
 *    this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE MIPS TECHNOLOGIES, INC. ``AS IS'' AND
 * ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED.  IN NO EVENT SHALL THE MIPS TECHNOLOGIES, INC. BE LIABLE
 * FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
 * DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
 * OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 * LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
 * OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
 * SUCH DAMAGE.
 *
 * Authors:  Stanislav Ocovaj (socovaj@mips.com)
 *           Goran Cordasic   (goran@mips.com)
 *           Djordje Pesut    (djordje@mips.com)
 *
 * This file is part of FFmpeg.
 *
 * FFmpeg is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 2.1 of the License, or (at your option) any later version.
 *
 * FFmpeg is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with FFmpeg; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
 */

/**
 * @file
 * definitions and initialization of LUT table for FFT
 */
#include "libavcodec/fft_table.h"

const int32_t ff_w_tab_sr[MAX_FFT_SIZE/(4*16)] = {
2147483647, 2147483016, 2147481121, 2147477963, 2147473542, 2147467857, 2147460908, 2147452697,
2147443222, 2147432484, 2147420483, 2147407218, 2147392690, 2147376899, 2147359845, 2147341527,
2147321946, 2147301102, 2147278995, 2147255625, 2147230991, 2147205094, 2147177934, 2147149511,
2147119825, 2147088876, 2147056664, 2147023188, 2146988450, 2146952448, 2146915184, 2146876656,
2146836866, 2146795813, 2146753497, 2146709917, 2146665076, 2146618971, 2146571603, 2146522973,
2146473080, 2146421924, 2146369505, 2146315824, 2146260881, 2146204674, 2146147205, 2146088474,
2146028480, 2145967224, 2145904705, 2145840924, 2145775880, 2145709574, 2145642006, 2145573176,
2145503083, 2145431729, 2145359112, 2145285233, 2145210092, 2145133690, 2145056025, 2144977098,
2144896910, 2144815460, 2144732748, 2144648774, 2144563539, 2144477042, 2144389283, 2144300264,
2144209982, 2144118439, 2144025635, 2143931570, 2143836244, 2143739656, 2143641807, 2143542697,
2143442326, 2143340694, 2143237802, 2143133648, 2143028234, 2142921559, 2142813624, 2142704427,
2142593971, 2142482254, 2142369276, 2142255039, 2142139541, 2142022783, 2141904764, 2141785486,
2141664948, 2141543150, 2141420092, 2141295774, 2141170197, 2141043360, 2140915264, 2140785908,
2140655293, 2140523418, 2140390284, 2140255892, 2140120240, 2139983329, 2139845159, 2139705730,
2139565043, 2139423097, 2139279892, 2139135429, 2138989708, 2138842728, 2138694490, 2138544994,
2138394240, 2138242228, 2138088958, 2137934430, 2137778644, 2137621601, 2137463301, 2137303743,
2137142927, 2136980855, 2136817525, 2136652938, 2136487095, 2136319994, 2136151637, 2135982023,
2135811153, 2135639026, 2135465642, 2135291003, 2135115107, 2134937956, 2134759548, 2134579885,
2134398966, 2134216791, 2134033361, 2133848675, 2133662734, 2133475538, 2133287087, 2133097381,
2132906420, 2132714204, 2132520734, 2132326009, 2132130030, 2131932796, 2131734309, 2131534567,
2131333572, 2131131322, 2130927819, 2130723062, 2130517052, 2130309789, 2130101272, 2129891502,
2129680480, 2129468204, 2129254676, 2129039895, 2128823862, 2128606576, 2128388038, 2128168248,
2127947206, 2127724913, 2127501367, 2127276570, 2127050522, 2126823222, 2126594672, 2126364870,
2126133817, 2125901514, 2125667960, 2125433155, 2125197100, 2124959795, 2124721240, 2124481435,
2124240380, 2123998076, 2123754522, 2123509718, 2123263666, 2123016364, 2122767814, 2122518015,
2122266967, 2122014670, 2121761126, 2121506333, 2121250292, 2120993003, 2120734467, 2120474683,
2120213651, 2119951372, 2119687847, 2119423074, 2119157054, 2118889788, 2118621275, 2118351516,
2118080511, 2117808259, 2117534762, 2117260020, 2116984031, 2116706797, 2116428319, 2116148595,
2115867626, 2115585412, 2115301954, 2115017252, 2114731305, 2114444114, 2114155680, 2113866001,
2113575080, 2113282914, 2112989506, 2112694855, 2112398960, 2112101824, 2111803444, 2111503822,
2111202959, 2110900853, 2110597505, 2110292916, 2109987085, 2109680013, 2109371700, 2109062146,
2108751352, 2108439317, 2108126041, 2107811526, 2107495770, 2107178775, 2106860540, 2106541065,
2106220352, 2105898399, 2105575208, 2105250778, 2104925109, 2104598202, 2104270057, 2103940674,
2103610054, 2103278196, 2102945101, 2102610768, 2102275199, 2101938393, 2101600350, 2101261071,
2100920556, 2100578805, 2100235819, 2099891596, 2099546139, 2099199446, 2098851519, 2098502357,
2098151960, 2097800329, 2097447464, 2097093365, 2096738032, 2096381466, 2096023667, 2095664635,
2095304370, 2094942872, 2094580142, 2094216179, 2093850985, 2093484559, 2093116901, 2092748012,
2092377892, 2092006541, 2091633960, 2091260147, 2090885105, 2090508833, 2090131331, 2089752599,
2089372638, 2088991448, 2088609029, 2088225381, 2087840505, 2087454400, 2087067068, 2086678508,
2086288720, 2085897705, 2085505463, 2085111994, 2084717298, 2084321376, 2083924228, 2083525854,
2083126254, 2082725429, 2082323379, 2081920103, 2081515603, 2081109879, 2080702930, 2080294757,
2079885360, 2079474740, 2079062896, 2078649830, 2078235540, 2077820028, 2077403294, 2076985338,
2076566160, 2076145760, 2075724139, 2075301296, 2074877233, 2074451950, 2074025446, 2073597721,
2073168777, 2072738614, 2072307231, 2071874629, 2071440808, 2071005769, 2070569511, 2070132035,
2069693342, 2069253430, 2068812302, 2068369957, 2067926394, 2067481616, 2067035621, 2066588410,
2066139983, 2065690341, 2065239484, 2064787411, 2064334124, 2063879623, 2063423908, 2062966978,
2062508835, 2062049479, 2061588910, 2061127128, 2060664133, 2060199927, 2059734508, 2059267877,
2058800036, 2058330983, 2057860719, 2057389244, 2056916560, 2056442665, 2055967560, 2055491246,
2055013723, 2054534991, 2054055050, 2053573901, 2053091544, 2052607979, 2052123207, 2051637227,
2051150040, 2050661647, 2050172048, 2049681242, 2049189231, 2048696014, 2048201592, 2047705965,
2047209133, 2046711097, 2046211857, 2045711414, 2045209767, 2044706916, 2044202863, 2043697608,
2043191150, 2042683490, 2042174628, 2041664565, 2041153301, 2040640837, 2040127172, 2039612306,
2039096241, 2038578976, 2038060512, 2037540850, 2037019988, 2036497928, 2035974670, 2035450215,
2034924562, 2034397712, 2033869665, 2033340422, 2032809982, 2032278347, 2031745516, 2031211490,
2030676269, 2030139853, 2029602243, 2029063439, 2028523442, 2027982251, 2027439867, 2026896291,
2026351522, 2025805561, 2025258408, 2024710064, 2024160529, 2023609803, 2023057887, 2022504780,
2021950484, 2021394998, 2020838323, 2020280460, 2019721407, 2019161167, 2018599739, 2018037123,
2017473321, 2016908331, 2016342155, 2015774793, 2015206245, 2014636511, 2014065592, 2013493489,
2012920201, 2012345729, 2011770073, 2011193233, 2010615210, 2010036005, 2009455617, 2008874047,
2008291295, 2007707362, 2007122248, 2006535953, 2005948478, 2005359822, 2004769987, 2004178973,
2003586779, 2002993407, 2002398857, 2001803128, 2001206222, 2000608139, 2000008879, 1999408442,
1998806829, 1998204040, 1997600076, 1996994937, 1996388622, 1995781134, 1995172471, 1994562635,
1993951625, 1993339442, 1992726087, 1992111559, 1991495860, 1990878989, 1990260946, 1989641733,
1989021350, 1988399796, 1987777073, 1987153180, 1986528118, 1985901888, 1985274489, 1984645923,
1984016189, 1983385288, 1982753220, 1982119985, 1981485585, 1980850019, 1980213288, 1979575392,
1978936331, 1978296106, 1977654717, 1977012165, 1976368450, 1975723572, 1975077532, 1974430331,
1973781967, 1973132443, 1972481757, 1971829912, 1971176906, 1970522741, 1969867417, 1969210933,
1968553292, 1967894492, 1967234535, 1966573420, 1965911148, 1965247720, 1964583136, 1963917396,
1963250501, 1962582451, 1961913246, 1961242888, 1960571375, 1959898709, 1959224890, 1958549919,
1957873796, 1957196520, 1956518093, 1955838516, 1955157788, 1954475909, 1953792881, 1953108703,
1952423377, 1951736902, 1951049279, 1950360508, 1949670589, 1948979524, 1948287312, 1947593954,
1946899451, 1946203802, 1945507008, 1944809070, 1944109987, 1943409761, 1942708392, 1942005880,
1941302225, 1940597428, 1939891490, 1939184411, 1938476190, 1937766830, 1937056329, 1936344689,
1935631910, 1934917992, 1934202936, 1933486742, 1932769411, 1932050943, 1931331338, 1930610597,
1929888720, 1929165708, 1928441561, 1927716279, 1926989864, 1926262315, 1925533633, 1924803818,
1924072871, 1923340791, 1922607581, 1921873239, 1921137767, 1920401165, 1919663432, 1918924571,
1918184581, 1917443462, 1916701216, 1915957841, 1915213340, 1914467712, 1913720958, 1912973078,
1912224073, 1911473942, 1910722688, 1909970309, 1909216806, 1908462181, 1907706433, 1906949562,
1906191570, 1905432457, 1904672222, 1903910867, 1903148392, 1902384797, 1901620084, 1900854251,
1900087301, 1899319232, 1898550047, 1897779744, 1897008325, 1896235790, 1895462140, 1894687374,
1893911494, 1893134500, 1892356392, 1891577171, 1890796837, 1890015391, 1889232832, 1888449163,
1887664383, 1886878492, 1886091491, 1885303381, 1884514161, 1883723833, 1882932397, 1882139853,
1881346202, 1880551444, 1879755580, 1878958610, 1878160535, 1877361354, 1876561070, 1875759681,
1874957189, 1874153594, 1873348897, 1872543097, 1871736196, 1870928194, 1870119091, 1869308888,
1868497586, 1867685184, 1866871683, 1866057085, 1865241388, 1864424594, 1863606704, 1862787717,
1861967634, 1861146456, 1860324183, 1859500816, 1858676355, 1857850800, 1857024153, 1856196413,
1855367581, 1854537657, 1853706643, 1852874538, 1852041343, 1851207059, 1850371686, 1849535224,
1848697674, 1847859036, 1847019312, 1846178501, 1845336604, 1844493621, 1843649553, 1842804401,
1841958164, 1841110844, 1840262441, 1839412956, 1838562388, 1837710739, 1836858008, 1836004197,
1835149306, 1834293336, 1833436286, 1832578158, 1831718951, 1830858668, 1829997307, 1829134869,
1828271356, 1827406767, 1826541103, 1825674364, 1824806552, 1823937666, 1823067707, 1822196675,
1821324572, 1820451397, 1819577151, 1818701835, 1817825449, 1816947994, 1816069469, 1815189877,
1814309216, 1813427489, 1812544694, 1811660833, 1810775906, 1809889915, 1809002858, 1808114737,
1807225553, 1806335305, 1805443995, 1804551623, 1803658189, 1802763694, 1801868139, 1800971523,
1800073849, 1799175115, 1798275323, 1797374472, 1796472565, 1795569601, 1794665580, 1793760504,
1792854372, 1791947186, 1791038946, 1790129652, 1789219305, 1788307905, 1787395453, 1786481950,
1785567396, 1784651792, 1783735137, 1782817434, 1781898681, 1780978881, 1780058032, 1779136137,
1778213194, 1777289206, 1776364172, 1775438094, 1774510970, 1773582803, 1772653593, 1771723340,
1770792044, 1769859707, 1768926328, 1767991909, 1767056450, 1766119952, 1765182414, 1764243838,
1763304224, 1762363573, 1761421885, 1760479161, 1759535401, 1758590607, 1757644777, 1756697914,
1755750017, 1754801087, 1753851126, 1752900132, 1751948107, 1750995052, 1750040966, 1749085851,
1748129707, 1747172535, 1746214334, 1745255107, 1744294853, 1743333573, 1742371267, 1741407936,
1740443581, 1739478202, 1738511799, 1737544374, 1736575927, 1735606458, 1734635968, 1733664458,
1732691928, 1731718378, 1730743810, 1729768224, 1728791620, 1727813999, 1726835361, 1725855708,
1724875040, 1723893357, 1722910659, 1721926948, 1720942225, 1719956488, 1718969740, 1717981981,
1716993211, 1716003431, 1715012642, 1714020844, 1713028037, 1712034223, 1711039401, 1710043573,
1709046739, 1708048900, 1707050055, 1706050207, 1705049355, 1704047500, 1703044642, 1702040783,
1701035922, 1700030061, 1699023199, 1698015339, 1697006479, 1695996621, 1694985765, 1693973912,
1692961062, 1691947217, 1690932376, 1689916541, 1688899711, 1687881888, 1686863072, 1685843263,
1684822463, 1683800672, 1682777890, 1681754118, 1680729357, 1679703608, 1678676870, 1677649144,
1676620432, 1675590733, 1674560049, 1673528379, 1672495725, 1671462087, 1670427466, 1669391862,
1668355276, 1667317709, 1666279161, 1665239632, 1664199124, 1663157637, 1662115172, 1661071729,
1660027308, 1658981911, 1657935539, 1656888190, 1655839867, 1654790570, 1653740300, 1652689057,
1651636841, 1650583654, 1649529496, 1648474367, 1647418269, 1646361202, 1645303166, 1644244162,
1643184191, 1642123253, 1641061349, 1639998480, 1638934646, 1637869848, 1636804087, 1635737362,
1634669676, 1633601027, 1632531418, 1631460848, 1630389319, 1629316830, 1628243383, 1627168978,
1626093616, 1625017297, 1623940023, 1622861793, 1621782608, 1620702469, 1619621377, 1618539332,
1617456335, 1616372386, 1615287487, 1614201637, 1613114838, 1612027089, 1610938393, 1609848749,
1608758157, 1607666620, 1606574136, 1605480708, 1604386335, 1603291018, 1602194758, 1601097555,
1599999411, 1598900325, 1597800299, 1596699333, 1595597428, 1594494583, 1593390801, 1592286082,
1591180426, 1590073833, 1588966306, 1587857843, 1586748447, 1585638117, 1584526854, 1583414660,
1582301533, 1581187476, 1580072489, 1578956572, 1577839726, 1576721952, 1575603251, 1574483623,
1573363068, 1572241588, 1571119183, 1569995854, 1568871601, 1567746425, 1566620327, 1565493307,
1564365367, 1563236506, 1562106725, 1560976026, 1559844408, 1558711873, 1557578421, 1556444052,
1555308768, 1554172569, 1553035455, 1551897428, 1550758488, 1549618636, 1548477872, 1547336197,
1546193612, 1545050118, 1543905714, 1542760402, 1541614183, 1540467057, 1539319024, 1538170087,
1537020244, 1535869497, 1534717846, 1533565293, 1532411837, 1531257480, 1530102222, 1528946064,
1527789007, 1526631051, 1525472197, 1524312445, 1523151797, 1521990252, 1520827813, 1519664478,
1518500250, 1517335128, 1516169114, 1515002208, 1513834411, 1512665723, 1511496145, 1510325678,
1509154322, 1507982079, 1506808949, 1505634932, 1504460029, 1503284242, 1502107570, 1500930014,
1499751576, 1498572255, 1497392053, 1496210969, 1495029006, 1493846163, 1492662441, 1491477842,
1490292364, 1489106011, 1487918781, 1486730675, 1485541696, 1484351842, 1483161115, 1481969516,
1480777044, 1479583702, 1478389489, 1477194407, 1475998456, 1474801636, 1473603949, 1472405394,
1471205974, 1470005688, 1468804538, 1467602523, 1466399645, 1465195904, 1463991302, 1462785838,
1461579514, 1460372329, 1459164286, 1457955385, 1456745625, 1455535009, 1454323536, 1453111208,
1451898025, 1450683988, 1449469098, 1448253355, 1447036760, 1445819314, 1444601017, 1443381870,
1442161874, 1440941030, 1439719338, 1438496799, 1437273414, 1436049184, 1434824109, 1433598189,
1432371426, 1431143821, 1429915374, 1428686085, 1427455956, 1426224988, 1424993180, 1423760534,
1422527051, 1421292730, 1420057574, 1418821582, 1417584755, 1416347095, 1415108601, 1413869275,
1412629117, 1411388129, 1410146309, 1408903661, 1407660183, 1406415878, 1405170745, 1403924785,
1402678000, 1401430389, 1400181954, 1398932695, 1397682613, 1396431709, 1395179984, 1393927438,
1392674072, 1391419886, 1390164882, 1388909060, 1387652422, 1386394966, 1385136696, 1383877610,
1382617710, 1381356997, 1380095472, 1378833134, 1377569986, 1376306026, 1375041258, 1373775680,
1372509294, 1371242101, 1369974101, 1368705296, 1367435685, 1366165269, 1364894050, 1363622028,
1362349204, 1361075579, 1359801152, 1358525926, 1357249901, 1355973077, 1354695455, 1353417037,
1352137822, 1350857812, 1349577007, 1348295409, 1347013017, 1345729833, 1344445857, 1343161090,
1341875533, 1340589187, 1339302052, 1338014129, 1336725419, 1335435923, 1334145641, 1332854574,
1331562723, 1330270089, 1328976672, 1327682474, 1326387494, 1325091734, 1323795195, 1322497877,
1321199781, 1319900907, 1318601257, 1317300832, 1315999631, 1314697657, 1313394909, 1312091388,
1310787095, 1309482032, 1308176198, 1306869594, 1305562222, 1304254082, 1302945174, 1301635500,
1300325060, 1299013855, 1297701886, 1296389154, 1295075659, 1293761402, 1292446384, 1291130606,
1289814068, 1288496772, 1287178717, 1285859905, 1284540337, 1283220013, 1281898935, 1280577102,
1279254516, 1277931177, 1276607086, 1275282245, 1273956653, 1272630312, 1271303222, 1269975384,
1268646800, 1267317469, 1265987392, 1264656571, 1263325005, 1261992697, 1260659646, 1259325853,
1257991320, 1256656047, 1255320034, 1253983283, 1252645794, 1251307568, 1249968606, 1248628909,
1247288478, 1245947312, 1244605414, 1243262783, 1241919421, 1240575329, 1239230506, 1237884955,
1236538675, 1235191668, 1233843935, 1232495475, 1231146291, 1229796382, 1228445750, 1227094395,
1225742318, 1224389521, 1223036002, 1221681765, 1220326809, 1218971135, 1217614743, 1216257636,
1214899813, 1213541275, 1212182024, 1210822059, 1209461382, 1208099993, 1206737894, 1205375085,
1204011567, 1202647340, 1201282407, 1199916766, 1198550419, 1197183368, 1195815612, 1194447153,
1193077991, 1191708127, 1190337562, 1188966297, 1187594332, 1186221669, 1184848308, 1183474250,
1182099496, 1180724046, 1179347902, 1177971064, 1176593533, 1175215310, 1173836395, 1172456790,
1171076495, 1169695512, 1168313840, 1166931481, 1165548435, 1164164704, 1162780288, 1161395188,
1160009405, 1158622939, 1157235792, 1155847964, 1154459456, 1153070269, 1151680403, 1150289860,
1148898640, 1147506745, 1146114174, 1144720929, 1143327011, 1141932420, 1140537158, 1139141224,
1137744621, 1136347348, 1134949406, 1133550797, 1132151521, 1130751579, 1129350972, 1127949701,
1126547765, 1125145168, 1123741908, 1122337987, 1120933406, 1119528166, 1118122267, 1116715710,
1115308496, 1113900627, 1112492101, 1111082922, 1109673089, 1108262603, 1106851465, 1105439676,
1104027237, 1102614148, 1101200410, 1099786025, 1098370993, 1096955314, 1095538991, 1094122023,
1092704411, 1091286156, 1089867259, 1088447722, 1087027544, 1085606726, 1084185270, 1082763176,
1081340445, 1079917078, 1078493076, 1077068439, 1075643169, 1074217266, 1072790730, 1071363564,
1069935768, 1068507342, 1067078288, 1065648605, 1064218296, 1062787361, 1061355801, 1059923616,
1058490808, 1057057377, 1055623324, 1054188651, 1052753357, 1051317443, 1049880912, 1048443763,
1047005996, 1045567615, 1044128617, 1042689006, 1041248781, 1039807944, 1038366495, 1036924436,
1035481766, 1034038487, 1032594600, 1031150105, 1029705004, 1028259297, 1026812985, 1025366069,
1023918550, 1022470428, 1021021705, 1019572382, 1018122458, 1016671936, 1015220816, 1013769098,
1012316784, 1010863875, 1009410370, 1007956272, 1006501581, 1005046298, 1003590424, 1002133959,
1000676905, 999219262, 997761031, 996302214, 994842810, 993382821, 991922248, 990461091,
988999351, 987537030, 986074127, 984610645, 983146583, 981681943, 980216726, 978750932,
977284562, 975817617, 974350098, 972882006, 971413342, 969944106, 968474300, 967003923,
965532978, 964061465, 962589385, 961116739, 959643527, 958169751, 956695411, 955220508,
953745043, 952269017, 950792431, 949315286, 947837582, 946359321, 944880503, 943401129,
941921200, 940440717, 938959681, 937478092, 935995952, 934513261, 933030021, 931546231,
930061894, 928577010, 927091579, 925605603, 924119082, 922632018, 921144411, 919656262,
918167572, 916678342, 915188572, 913698265, 912207419, 910716038, 909224120, 907731667,
906238681, 904745161, 903251110, 901756526, 900261413, 898765769, 897269597, 895772898,
894275671, 892777918, 891279640, 889780838, 888281512, 886781663, 885281293, 883780402,
882278992, 880777062, 879274614, 877771649, 876268167, 874764170, 873259659, 871754633,
870249095, 868743045, 867236484, 865729413, 864221832, 862713743, 861205147, 859696043,
858186435, 856676321, 855165703, 853654582, 852142959, 850630835, 849118210, 847605086,
846091463, 844577343, 843062726, 841547612, 840032004, 838515901, 836999305, 835482217,
833964638, 832446567, 830928007, 829408958, 827889422, 826369398, 824848888, 823327893,
821806413, 820284450, 818762005, 817239078, 815715670, 814191782, 812667415, 811142571,
809617249, 808091450, 806565177, 805038429, 803511207, 801983513, 800455346, 798926709,
797397602, 795868026, 794337982, 792807470, 791276492, 789745049, 788213141, 786680769,
785147934, 783614638, 782080880, 780546663, 779011986, 777476851, 775941259, 774405210,
772868706, 771331747, 769794334, 768256469, 766718151, 765179382, 763640164, 762100496,
760560380, 759019816, 757478806, 755937350, 754395449, 752853105, 751310318, 749767089,
748223418, 746679308, 745134758, 743589770, 742044345, 740498483, 738952186, 737405453,
735858287, 734310688, 732762657, 731214195, 729665303, 728115982, 726566232, 725016055,
723465451, 721914422, 720362968, 718811090, 717258790, 715706067, 714152924, 712599360,
711045377, 709490976, 707936158, 706380923, 704825272, 703269207, 701712728, 700155836,
698598533, 697040818, 695482694, 693924160, 692365218, 690805869, 689246113, 687685952,
686125387, 684564417, 683003045, 681441272, 679879097, 678316522, 676753549, 675190177,
673626408, 672062243, 670497682, 668932727, 667367379, 665801638, 664235505, 662668981,
661102068, 659534766, 657967075, 656398998, 654830535, 653261686, 651692453, 650122837,
648552838, 646982457, 645411696, 643840556, 642269036, 640697139, 639124865, 637552215,
635979190, 634405791, 632832018, 631257873, 629683357, 628108471, 626533215, 624957590,
623381598, 621805239, 620228514, 618651424, 617073971, 615496154, 613917975, 612339436,
610760536, 609181276, 607601658, 606021683, 604441352, 602860664, 601279623, 599698227,
598116479, 596534378, 594951927, 593369126, 591785976, 590202477, 588618632, 587034440,
585449903, 583865021, 582279796, 580694229, 579108320, 577522070, 575935480, 574348552,
572761285, 571173682, 569585743, 567997469, 566408860, 564819919, 563230645, 561641039,
560051104, 558460839, 556870245, 555279324, 553688076, 552096502, 550504604, 548912382,
547319836, 545726969, 544133781, 542540273, 540946445, 539352300, 537757837, 536163058,
534567963, 532972554, 531376831, 529780796, 528184449, 526587791, 524990824, 523393547,
521795963, 520198072, 518599875, 517001373, 515402566, 513803457, 512204045, 510604332,
509004318, 507404005, 505803394, 504202485, 502601279, 500999778, 499397982, 497795892,
496193509, 494590835, 492987869, 491384614, 489781069, 488177236, 486573117, 484968710,
483364019, 481759043, 480153784, 478548243, 476942419, 475336316, 473729932, 472123270,
470516330, 468909114, 467301622, 465693854, 464085813, 462477499, 460868912, 459260055,
457650927, 456041530, 454431865, 452821933, 451211734, 449601270, 447990541, 446379549,
444768294, 443156777, 441545000, 439932963, 438320667, 436708113, 435095303, 433482236,
431868915, 430255339, 428641511, 427027430, 425413098, 423798515, 422183684, 420568604,
418953276, 417337703, 415721883, 414105819, 412489512, 410872962, 409256170, 407639137,
406021865, 404404353, 402786604, 401168618, 399550396, 397931939, 396313247, 394694323,
393075166, 391455778, 389836160, 388216313, 386596237, 384975934, 383355404, 381734649,
380113669, 378492466, 376871039, 375249392, 373627523, 372005435, 370383128, 368760603,
367137861, 365514903, 363891730, 362268343, 360644742, 359020930, 357396906, 355772673,
354148230, 352523578, 350898719, 349273654, 347648383, 346022908, 344397230, 342771348,
341145265, 339518981, 337892498, 336265816, 334638936, 333011859, 331384586, 329757119,
328129457, 326501602, 324873555, 323245317, 321616889, 319988272, 318359466, 316730474,
315101295, 313471930, 311842381, 310212649, 308582734, 306952638, 305322361, 303691904,
302061269, 300430456, 298799466, 297168301, 295536961, 293905447, 292273760, 290641901,
289009871, 287377671, 285745302, 284112765, 282480061, 280847190, 279214155, 277580955,
275947592, 274314066, 272680379, 271046532, 269412525, 267778360, 266144038, 264509558,
262874923, 261240134, 259605191, 257970095, 256334847, 254699448, 253063900, 251428203,
249792358, 248156366, 246520228, 244883945, 243247518, 241610947, 239974235, 238337382,
236700388, 235063255, 233425984, 231788575, 230151030, 228513350, 226875535, 225237587,
223599506, 221961294, 220322951, 218684479, 217045878, 215407149, 213768293, 212129312,
210490206, 208850976, 207211624, 205572149, 203932553, 202292838, 200653003, 199013051,
197372981, 195732795, 194092495, 192452080, 190811551, 189170911, 187530159, 185889297,
184248325, 182607245, 180966058, 179324764, 177683365, 176041861, 174400254, 172758544,
171116733, 169474820, 167832808, 166190698, 164548489, 162906184, 161263783, 159621287,
157978697, 156336015, 154693240, 153050374, 151407418, 149764374, 148121241, 146478021,
144834714, 143191323, 141547847, 139904288, 138260647, 136616925, 134973122, 133329239,
131685278, 130041240, 128397125, 126752935, 125108670, 123464332, 121819921, 120175438,
118530885, 116886262, 115241570, 113596810, 111951983, 110307091, 108662134, 107017112,
105372028, 103726882, 102081675, 100436408,  98791081,  97145697,  95500255,  93854758,
 92209205,  90563597,  88917937,  87272224,  85626460,  83980645,  82334782,  80688869,
 79042909,  77396903,  75750851,  74104755,  72458615,  70812432,  69166208,  67519943,
 65873638,  64227295,  62580914,  60934496,  59288042,  57641553,  55995030,  54348475,
 52701887,  51055268,  49408620,  47761942,  46115236,  44468503,  42821744,  41174960,
 39528151,  37881320,  36234466,  34587590,  32940695,  31293780,  29646846,  27999895,
 26352928,  24705945,  23058947,  21411936,  19764913,  18117878,  16470832,  14823776,
 13176712,  11529640,   9882561,   8235476,   6588387,   4941294,   3294197,   1647099
};

uint16_t ff_fft_offsets_lut[21845];

void ff_fft_lut_init(uint16_t *table, int off, int size, int *index)
{
    if (size < 16) {
        table[*index] = off >> 2;
        (*index)++;
    }
    else {
        ff_fft_lut_init(table, off, size>>1, index);
        ff_fft_lut_init(table, off+(size>>1), size>>2, index);
        ff_fft_lut_init(table, off+3*(size>>2), size>>2, index);
    }
}
