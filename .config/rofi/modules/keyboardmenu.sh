set -e
set -u

#All supported choices
all=(us rs rs-latin)

# By default, show all (i.e., just copy the array)
show=("${all[@]}")

declare -A texts
texts[us]="US layout"
texts[rs]="Serbian cyrillic"
texts[rs-latin]="Serbian latin"


if [ -z "${ROFI_OUTSIDE}" ]
then
    echo "run this script in rofi".
    exit
fi

echo -en "\x00no-custom\x1ffalse\n"
echo -en "\x00data\x1fmonkey do, monkey did\n"
echo -en "\x00use-hot-keys\x1ftrue\n"
echo -en "${ROFI_RETV}rs-latin"

if [ -n "${ROFI_INFO}" ]
then
    echo "my info: ${ROFI_INFO} "
fi
if [ -n "${ROFI_DATA}" ]
then
    echo "my data: ${ROFI_DATA} "
fi

setxkbmap $ROFI_RETV
