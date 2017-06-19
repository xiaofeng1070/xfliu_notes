#!/usr/bin/perl

#----  parse the directory of each case ----
@log_list = `ls */*.out`;


my @passed_log_array;
my @failed_log_array;
my @unknown_log_array;

my $log_name;

foreach (@log_list){
    open(FH, $_);
    $log_name = $_;
    while(<FH>) {
        if(/STATUS=PASSED/){
	    push(@passed_log_array, $log_name);
	    $unknown_flag = 0;
	    last;
	} elsif(/STATUS=FAILED/){
	    push(@failed_log_array, $log_name);
	    $unknown_flag = 0;
	    last;
	} else {
	    $unknown_flag = 1;
	}
    }
    if($unknown_flag == 1) {
    	push(@unknown_log_array, $log_name);
    	$unknown_flag = 0;
    }
}

foreach (@passed_log_array){
    print "PASSED log is $_";
}

foreach (@failed_log_array){
    print "FAILED log is $_";
}

foreach (@unknown_log_array){
    print "UNKNOWN log is $_";
}

