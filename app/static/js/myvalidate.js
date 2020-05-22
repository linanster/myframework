function validate_required(field,alerttxt)
{
with (field)
  {
  if (value==null||value=="")
    {alert(alerttxt);return false}
  else {return true}
  }
}

function validate_format(field,alerttxt)
{
with (field)
  {
    var macReg=/^[1-9][0-9]{4}$/;
    if (macReg.test(value))
      {return true}
    else if (value.length == 0)
      {return true}
    else
      {alert(alerttxt);return false}
  }
}

function validate_form(thisform)
{
with (thisform)
  {
  if (validate_required(devicecode,"请选择设备类型!")==false)
    {devicecode.focus();return false}
   
  if (validate_required(totalcount,"请选择设备数量!")==false)
    {totalcount.focus();return false}
   
  // if (validate_required(fwversion,"请输入固件版本号!")==false)
  //   {fwversion.focus();return false}
   
  if (validate_format(fwversion,"固件版本号格式错误!")==false)
    {fwversion.focus();return false}
  }
}

