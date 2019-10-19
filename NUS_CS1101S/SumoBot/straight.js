const ML = ev3_motorD();
const MR = ev3_motorA();

function check_connected(){

	if ( (ev3_connected(ML)) && (ev3_connected(MR)) ) {
		display("connected left and right");
		return true;
	} 
	else {
		if ( !ev3_connected(ML) ) {
			display("missing left motor");
		} else {}

		if ( !ev3_connected(MR) ) {
			display("missing right motor");
		} else {}

		return false;
	}
}


function move10() {
	if (check_connected()) {
		ev3_runForDistance(MR, 195, 200);
		ev3_runForDistance(ML, 195, 200);
	}

	else {
		display("error: check connectivity");
	}

	return 0;
}

move10();