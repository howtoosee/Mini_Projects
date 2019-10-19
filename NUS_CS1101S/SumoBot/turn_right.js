const ML = ev3_motorD();
const MR = ev3_motorA();


function turn_90() {
	ev3_runForDistance(MR, 225,  200);
	ev3_runForDistance(ML, -225, 200);

	return 0;
}

turn_90();