const mL = ev3_motorD();
const mR = ev3_motorA();

const colour = ev3_colorSensor();
 

function get_int() {
	return ev3_reflectedLightIntensity(colour);
}


function in_line() {
	let int = get_int();
	return int <= 10;
}


function straight(x, time) {
	ev3_runForTime(mL, time, x*200);
	ev3_runForTime(mR, time, x*200);
}


function turn() {
	ev3_runForTime(mL, 400, 0);
	ev3_runForTime(mR, 400, -200);
}


function touch_line() {
	let int = get_int();
	return 10 > int;
}

function forward() {
	straight(1,200);
}


function main() {

	while(true) {
		ev3_runUntil(touch_line, forward);
		turn();
		ev3_pause(400);
	}

	return 0;
}


main();


