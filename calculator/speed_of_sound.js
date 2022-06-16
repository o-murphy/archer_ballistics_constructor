// Code from: Dr Richard Lord - http://www.npl.co.uk/acoustics/techguides/speedair
// Based on the approximate formula found in
// Owen Cramer, "The variation of the specific heat ratio and the speed of sound in air with temperature, pressure, humidity, and CO2 concentration",
// The Journal of the Acoustical Society of America (JASA), J. Acoust. Soc. Am. 93(5) p. 2510-2516; formula at p. 2514.
// Saturation vapour pressure found in
// Richard S. Davis, "Equation for the Determination of the Density of Moist Air (1981/91)", Metrologia, 29, p. 67-70, 1992,
// and a mole fraction of carbon dioxide of 0.0004.
// The mole fraction is simply an expression of the number of moles of a compound divided by the total number of moles of all the compounds present in the gas.

function Log10(x) {
    return Math.log(x) / Math.log(10);
}
function roundto(x, dp) {
    return (Math.round(x * Math.pow(10, dp)) / Math.pow(10, dp));
}
function sqr(x) {
    return Math.pow(x, 2);
}
function Calculate_OnClick() {
    // main body of program to calculate speed of sound in humid air
    var T;// temperature deg C
    var P;// pressure
    var Rh;// relative humidity
    var C;// speed
    var Xc, Xw;// Mole fraction of carbon dioxide and water vapour
    var H;// respectively molecular concentration of water vapour
    var C1;// Intermediate calculations
    var C2;
    var C3;
    var ENH;
    var PSV;
    var PSV1;
    var PSV2;
    var T_kel;// ambient temperature (Kelvin)
    var StrMsg;// alert text
    var Kelvin = 273.15;// For converting to Kelvin
    var e = 2.71828182845904523536;
    // Getvariables from form
    T = Number(document.humidity.Temperature.value);
    P = Number(document.humidity.Pressure.value) * 1000.0;
    Rh = Number(document.humidity.Hum.value);
    // Check that sensible numbers were entered
    if ((Rh > 100) || (Rh < 0)) {
        StrMsg = "Relative humidity must be between 0 and 100%";
        document.humidity.Hum.focus = true;
        alert('Data out of range: ' + StrMsg);
        return false;
    }
    T_kel = Kelvin + T;// Measured ambient temp
    // Molecular concentration of water vapour calculated from Rh
    // using Giacomos method by Davis (1991) as implemented in DTU report 11b-1997
    ENH = 3.141593 * Math.pow(10, -8) * P + 1.00062 + sqr(T) * 5.6 * Math.pow(10, -7);
    // These commented lines correspond to values used in Cramer (Appendix)
    // PSV1 = sqr(T_kel)*1.2811805*Math.pow(10,-5)-1.9509874*Math.pow(10,-2)*T_kel ;
    // PSV2 = 34.04926034-6.3536311*Math.pow(10,3)/T_kel;
    PSV1 = sqr(T_kel) * 1.2378847 * Math.pow(10, -5) - 1.9121316 * Math.pow(10, -2) * T_kel;
    PSV2 = 33.93711047 - 6.3431645 * Math.pow(10, 3) / T_kel;
    PSV = Math.pow(e, PSV1) * Math.pow(e, PSV2);
    H = Rh * ENH * PSV / P;
    Xw = H / 100.0;
    // Xc = 314.0*Math.pow(10,-6);
    Xc = 400.0 * Math.pow(10, -6);
    // Speed calculated using the method
    // of Cramer from JASA vol 93 p. 2510
    C1 = 0.603055 * T + 331.5024 - sqr(T) * 5.28 * Math.pow(10, -4) + (0.1495874 * T + 51.471935 - sqr(T) * 7.82 * Math.pow(10, -4)) * Xw;
    C2 = (-1.82 * Math.pow(10, -7) + 3.73 * Math.pow(10, -8) * T - sqr(T) * 2.93 * Math.pow(10, -10)) * P + (-85.20931 - 0.228525 * T + sqr(T) * 5.91 * Math.pow(10, -5)) * Xc;
    C3 = sqr(Xw) * 2.835149 - sqr(P) * 2.15 * Math.pow(10, -13) + sqr(Xc) * 29.179762 + 4.86 * Math.pow(10, -4) * Xw * P * Xc;
    C = C1 + C2 - C3;
    // return C to the document
    document.humidity.Speed.value = roundto(C, 2);
}
// end Calculation of speed of sound in humid air
