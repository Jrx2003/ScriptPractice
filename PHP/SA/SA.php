<?php
// Set the content type
header("Content-type: text/html");

// echo rand() . " " . getrandmax();
// exit;

// Print the style
echo "<style> td {font-size:8pt} </style>";

// $cgidat = $_SERVER['QUERY_STRING'];
parse_str($cgidat, $cd);

// Initialize the parameters
$n = isset($cd["n"]) ? $cd["n"] : 16;
$m = isset($cd["m"]) ? $cd["m"] : 4;
$smooth = isset($cd["smooth"]) ? $cd["smooth"] : 8;
$anneal = isset($cd["anneal"]) ? $cd["anneal"] : 1;
$maxep = isset($cd["maxep"]) ? $cd["maxep"] : 100;
$skip = isset($cd["skip"]) ? $cd["skip"] : 1;

srand();
// echo "m=$m\n"; 

// Initialize variables and display
init();

echo "classes = " . $m;
display($p);

for ($ep = 1; $ep <= $maxep; $ep++) {
    echo "\tepoch" . $ep;
    
    if ($anneal && rand() / getrandmax() < exp(-$ep / $smooth)) {
        $randstep = 1;
        $jbest = $ibest = rand(1, $n);
        while ($ibest == $jbest) $jbest = rand(1, $n);
        echo "<font color=red>taking random step</font>";
    } else {
        $randstep = 0;
        $jbest = $ibest = rand(1, $n);
        while ($ibest == $jbest) $jbest = rand(1, $n);

        $best = "";
        for ($i = 1; $i <= $n; $i++) {
            for ($j = $i + 1; $j <= $n; $j++) {
                if ($skip && rand() / getrandmax() < exp(-$ep / $smooth)) {
                    echo "<font color=red>(skipping $i,$j)</font>";
                    continue;
                }
                swap($i, $j);
                $ts = score();
                if ($best == "" || $ts > $best) {
                    $best = $ts;
                    $ibest = $i;
                    $jbest = $j;
                }
            }
        }
        if (!$anneal && !$skip && $best < $lastbest) exit;
        $lastbest = $best;
    }

    swap($ibest, $jbest);

    // Commit
    for ($i = 1; $i <= $n; $i++) {
        for ($j = 1; $j <= $n; $j++) {
            $p[$i][$j] = $temp[$i][$j];
        }
    }

    if ($randstep) {
        $lastbest = $best = score();
        echo "random swap is " . $who[$ibest] . " " . $who[$jbest];
        echo "score is " . $best;
    } else {
        echo "best swap is " . $who[$ibest] . " " . $who[$jbest];
        echo "score is " . $best;
    }

    // Track the changes
    $tempwho = $who[$ibest];
    $who[$ibest] = $who[$jbest];
    $who[$jbest] = $tempwho;
    
    display($p);
}

function display($arr) {
    global $n, $who;

    // JavaScript function to update the info-box when a cell is clicked
    echo "<script>
        function updateInfo(rgb, preF) {
            document.getElementById('info-box').innerHTML = 
                '<strong>RGB:</strong> ' + rgb + '<br><strong>Pre-F:</strong> ' + preF;
        }
    </script>";

    // Create an info-box that will display the clicked cell's RGB and Pre-F values
    echo "<div id='info-box' style='border: 1px solid black; padding: 10px; width: 150px; margin-bottom: 10px;'>
        Click on a box to see RGB and Pre-F values.
    </div>";

    echo "<table border=1 cellpadding=0 cellspacing=0>";
    echo "<tr><td></td>";
    for ($j = 1; $j <= $n; $j++) echo "<td>" . $who[$j] . "</td>";
    echo "</tr>";

    for ($i = 1; $i <= $n; $i++) {
        echo "<tr><td>" . $who[$i] . "</td>";
        for ($j = 1; $j <= $n; $j++) {
            $color = f($arr[$i][$j]);
            $value = $arr[$i][$j];

            // Create a table cell with a background color and an onclick event
            echo "<td bgcolor='$color' onclick=\"updateInfo('$color', '$value')\" width=10 height=5>&nbsp;</td>";
        }
        echo "</tr>";
    }
    echo "</table>";
}


function abs_val($x) {
    return $x < 0 ? -$x : $x;
}

function f($n) {
    $raw = (int)($n * 60.0 + 0.5);
    if ($raw < 0) $raw = 0;
    if ($raw > 255) $raw = 255;

    // Red stays at 255 for a yellow tint
    $red = 255;
    // Green varies based on brightness, reducing the influence of blue
    $green = $raw;  
    // Blue remains 0 to maintain the yellow hue
    $blue = 0;

    // Convert to hex format
    return sprintf("#%02X%02X%02X", $red, $green, $blue);
}


function swap($i, $j) {
    global $n, $p, $key, $temp;
    
    for ($ii = 1; $ii <= $n; $ii++) $key[$ii] = $ii;
    $key[$i] = $j;
    $key[$j] = $i;

    for ($ii = 1; $ii <= $n; $ii++) {
        for ($jj = 1; $jj <= $n; $jj++) {
            $temp[$ii][$jj] = $p[$key[$ii]][$key[$jj]];
        }
    }
}

function score() {
    global $n, $temp, $who;

    $res = 0;
    for ($i = 1; $i <= $n; $i++) {
        for ($j = 1; $j <= $n; $j++) {
            $res -= $temp[$i][$j] / (0.1 + abs_val($i - $j));
        }
    }
    return 1000 - $res;
}

function init() {
    global $m, $n, $p, $who;
    
    for ($i = 1; $i <= $n; $i++) $who[$i] = $i;
    for ($i = 1; $i <= $n; $i++) {
        for ($j = 1; $j <= $n; $j++) {
            if (isset($p[$j][$i])) {
                $p[$i][$j] = $p[$j][$i];
                continue;
            }
            $kmax = 5;
// echo "m=$m\n"; 
            if ($i % $m == $j % $m) $kmax *= 3;
            $diff = abs_val($i % $m - $j % $m);
            if ($diff < $m / 2) $kmax += $diff;

            for ($k = 1; $k <= $kmax; $k++) {
                $p[$i][$j] += rand() / getrandmax();
            }
        }
    }
}

function w($i) {
    global $n;
    if ($i >= 1 && $i <= $n) return $i;
    if ($i < 1) return $n;
    if ($i > $n) return 1;
}
?>
