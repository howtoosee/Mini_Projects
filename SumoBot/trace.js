const mL = ev3_motorD();
const mR = ev3_motorA();

const color = ev3_colorSensor();


const time = 25;
const dist = time;

const fwd_spd = 75;
const rev_spd = 40;


function get_int() {
	return ev3_reflectedLightIntensity(color);
}


function out_of_line() {
	let int = get_int();
	return int > 12;
}


function in_line() {
	let int = get_int();
	return int < 8;
}


function wiggle(dir) {

	if (dir === "L") {
		ev3_runForDistance(mL, dist, rev_spd);
		ev3_runForDistance(mR, -dist, fwd_spd);
	}
	else {
		ev3_runForDistance(mL, -dist, fwd_spd);
		ev3_runForDistance(mR, dist, rev_spd);
	}
}


function forward() {
	ev3_runForDistance(mR, -dist, fwd_spd);
	ev3_runForDistance(mL, -dist, fwd_spd);

}


function wiggleL() {
	wiggle("L");
}


function wiggleR() {
	wiggle("R");
}


function main() {
    
	while(true) {
		let int = get_int();
		display(int);

		if (out_of_line()) {
			display("left");
			wiggleL();

		} else if (in_line()) {
			display("right");
			wiggleR();
			ev3_pause(time);

		} else {
			display("forward");
			forward();
		}


	}

	return 0;
}


main();
