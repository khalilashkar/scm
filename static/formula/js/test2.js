if (!$) {
    // Need this line because Django also provided jQuery and namespaced as django.jQuery
    $ = django.jQuery;
}
//////////////////////////////////////////////function to replace the urls  into links 
var text = $("#id_articls_link_1").val();
var text1=$("#id_summary_of_your_state").val();
text1=text
// text = text.replace(
//     /((http|https|ftp|ftps)\:\/\/[a-zA-Z0-9\-\.]+\.[a-zA-Z]{2,3}(\/\S*)?)/g,
//     '<a href="$1">$1</a>'
// );
//function to hide yes and no qustions from regestration admin interface
/////////////////////////////////////////////////////////////////////////
  $( document ).ready( function() {
    $(function () {
      if ($("#id_medical_state_inf").val() =='1') {
        $('label[for=id_medical_note_inf],#id_medical_note_inf').hide();
        
    }

        $('#id_medical_state_inf').change(function () {
          var medical=$("#id_medical_state_inf").val()
          switch(medical) {
            case '0':
              $('label[for=id_medical_note_inf],#id_medical_note_inf').show();
              break;
            case '1':
              $('label[for=id_medical_note_inf],#id_medical_note_inf').hide();
              break;             
            default:
              $('label[for=id_medical_note_inf],#id_medical_note_inf').hide();
                
          }    
    
        });        
    });
    });
//************************************************************ */ 
$( document ).ready( function() {
  $(function () {
    if ($('#id_paid_job').val() =='1') {
      $('label[for=id_name_of_company_paid],#id_name_of_company_paid').hide();
              
      
  }
        $('#id_paid_job').change(function () {
        var paid=$('#id_paid_job').val()
        switch(paid) {
          case '0':
            $('label[for=id_name_of_company_paid],#id_name_of_company_paid').show();
            break;
          case '1':
            $('label[for=id_name_of_company_paid],#id_name_of_company_paid').hide();
            break;             
          default:
            $('label[for=id_name_of_company_paid],#id_name_of_company_paid').hide();
              
        }    
  
      });        
  });
  });
//************************************************************************************ */
// hide volations case in the admin page 
  // $( document ).ready( function() {
  // $(function () {
  //   if ($('#id_violations').val() =='1') {
  //     $('label[for=id_kind_of_violation_1],#id_kind_of_violation_1').hide();
  //     $('label[for=id_date_of_violations_1],#id_date_of_violations_1').hide();       
  //     $('.datetimeshortcuts').hide();
  // }
  //       $('#id_violations').change(function () {
  //       var violation=$('#id_violations').val()
  //       switch(violation) {
  //         case '0':
  //           $('label[for=id_kind_of_violation_1],#id_kind_of_violation_1').show();
  //           $('label[for=id_date_of_violations_1],#id_date_of_violations_1').show();
  //           $('.datetimeshortcuts').show()
  //           break;
  //         case '1':
  //          $('label[for=id_kind_of_violation_1],#id_kind_of_violation_1').hide();
  //          $('label[for=id_date_of_violations_1],#id_date_of_violations_1').hide();
  //          $(this)('.datetimeshortcuts').hide()
  //           break;             
  //         default:
  //         $('label[for=id_kind_of_violation_1],#id_kind_of_violation_1').hide();
  //          $('label[for=id_date_of_violations_1],#id_date_of_violations_1').hide();
  //          $('.datetimeshortcuts').hide();

  //       }    
  
  //     });        
  // });
  // });
  //****************************************************************   */
  // paid show and hide
    $( document ).ready( function() {
      $(function () {
        if ($('#id_paid_job').val() =='1') {
          $('label[for=id_name_of_company_paid],#id_name_of_company_paid').hide();
                  
          
      }
            $('#id_paid_job').change(function () {
            var paid=$('#id_paid_job').val()
            switch(paid) {
              case '0':
                $('label[for=id_name_of_company_paid],#id_name_of_company_paid').show();
                break;
              case '1':
                $('label[for=id_name_of_company_paid],#id_name_of_company_paid').hide();
                break;             
              default:
                $('label[for=id_name_of_company_paid],#id_name_of_company_paid').hide();
                  
            }    
      
          });        
      });
      });
//************************************************************************************* */
// family state show/hide 
$( document ).ready( function() {
  $(function () {
    if ($('#id_family_state').val() =='عازب') {
      $('label[for=id_have_kids],#id_have_kids').hide();
              
      
  }
        $('#id_family_state').change(function () {
        var paid=$('#id_family_state').val()
        switch(paid) {
          case 'متزوج':
            $('label[for=id_have_kids],#id_have_kids').show();
            break;
          case 'عازب':
            $('label[for=id_have_kids],#id_have_kids').hide();
            break;             
          default:
            $('label[for=id_have_kids],#id_have_kids').hide();
              
        }    
  
      });        
  });
  });
//**************************************************************************************** */
// hide and show the media member block 
$( document ).ready( function() {
  $(function () {
    if ($('#id_org_memeber').val() =='1') {
      $('label[for=id_details],#id_details').hide();
              
      
  }
        $(' #id_org_memeber').change(function () {
        var paid=$('#id_org_memeber').val()
        switch(paid) {
          case '0':
            $('label[for=id_details],#id_details').show();
            break;
          case '1':
            $('label[for=id_details],#id_details').hide();
            break;             
          default:
            $('label[for=id_details],#id_details').hide();
              
        }    
  
      });        
  });
  });
//////////////////////////////////////////////////////////////////////////////////////////////
 $( document ).ready( function() {
        $(function () {
          if ($('#id_have_kids').val() =='1') {
            $('label[for=id_number_kids],#id_number_kids').hide();
            $('label[for=id_summary_of_recsituation],#id_summary_of_recsituation').hide();
            
            
        }
              $('#id_have_kids').change(function () {
              var kids=$('#id_have_kids').val()
              switch(kids) {
                case '0':
                  $('label[for=id_number_kids],#id_number_kids').show();
                  $('label[for=id_summary_of_recsituation],#id_summary_of_recsituation').show();
                    
                  break;
                case '1':
                  $('label[for=id_number_kids],#id_number_kids').hide();
                  $('label[for=id_summary_of_recsituation],#id_summary_of_recsituation').hide();
                  
                  break;             
                default:
                  $('label[for=id_number_kids],#id_number_kids').hide();
                  $('label[for=id_summary_of_recsituation],#id_summary_of_recsituation').hide();
                  
                    
              }    
        
            });        
        });
        });  
//********************************************************** */  
$( document ).ready( function() {
  $(function () {
    if ($('#id_relation_with_org').val() =='1') {
      $('label[for=id_number_kids],#id_number_kids').hide();
      $('label[for=id_summary_of_recsituation],#id_summary_of_recsituation').hide();
      
      
  }
        $('#id_relation_with_org').change(function () {
        var kids=$('#id_relation_with_org').val()
        switch(kids) {
          case '0':
            $('label[for=id_summary_of_relations],#id_summary_of_relations').show();
              
            break;
          case '1':
            $('label[for=id_summary_of_relations],#id_summary_of_relations').hide();
            break;             
          default:
            $('label[for=id_summary_of_relations],#id_summary_of_relations').hide();
              
        }    
  
      });        
  });
  }); 

///////////////////////////////////////////////////////////::
$( document ).ready( function() {
  $(function () {
    // $('.support').hide();
    // $('.supportchild').hide();
      $('#id_checking-0-result_of_verfication').change(function () {
        var support=$("#id_checking-0-result_of_verfication").val()
        switch(support) {
          case '0':
            $('.support').Show();
            $('.supportchild').show();
            $('.supportchild_cost').show();
            break;
          case '1':
            $('.support').hide();
            $('.supportchild').hide();
            $('.supportchild_cost').hide();
            break;             
          default:
            $('.support').hide();
            $('.supportchild').hide();
              
        }    
  
      });        
  });
  });
      
//   });
//   });
// // function to hide the cost from supportchils
// $( document ).ready( function() {
//   $(function () {
//     $('.supportchild_cost').hide();
//   // $('.abcdefgh').hide();
//       $('#id_type_of_dmande').change(function () {
//         $('.supportchild_cost').hide();
//         // $('.abcdefgh').hide();
//           if (this.options[this.selectedIndex].value =='0') {
            
//             $('.supportchild_cost').show();           
//           }
          
    
//       }); 
      
//   });
//   });
  
// function to note the years of experinces
$( document ).ready( function() {
  $(function () {
  // $('.abcdefgh').hide();
      $('#id_checking-0-number_of_year_exprince').change(function () {
        var years_exp=$("#id_checking-0-number_of_year_exprince").val()
        switch(years_exp) {
          case '0':
              $("#id_checking-0-note_of_year_experince").val('1');
            break;
          case '1':
              $("#id_checking-0-note_of_year_experince").val('2');
            break;
            case '2':
              $("#id_checking-0-note_of_year_experince").val('3');
            break;
            case '3':
            $("#id_checking-0-note_of_year_experince").val('0');
            break;
            
          default:
              $("#id_checking-0-note_of_year_experince").val('0');
              
        }    
  
      });        
  });
  });
//function to note the step2
$( document ).ready( function() {
    $(function () {
    // $('.abcdefgh').hide();
        $('#id_checking-0-rspect_legal_coppyright').change(function () {
          var coppy_right=$("#id_checking-0-rspect_legal_coppyright").val()
          switch(coppy_right) {
            case '0':
                $("#id_checking-0-mark_rspect_legal_coppyright").val('1');
              break;
            case '1':
                $("#id_checking-0-mark_rspect_legal_coppyright").val('0');
              break;             
            default:
                $("#id_checking-0-mark_rspect_legal_coppyright").val('0');
                
          }    
    
        });        
    });
    });
    ////////////////////////////////////
    $( document ).ready( function() {
        $(function () {
        // $('.abcdefgh').hide();
            $('#id_checking-0-rspect_coppyright').change(function () {
              var coppy_right=$("#id_checking-0-rspect_coppyright").val()
              switch(coppy_right) {
                case '0':
                    $("#id_checking-0-mark_rspect_coppyright").val('1');
                  break;
                case '1':
                    $("#id_checking-0-mark_rspect_coppyright").val('0');
                  break;             
                default:
                    $("#id_checking-0-mark_rspect_coppyright").val('0');
                    
              }    
        
            });        
        });
        });
////////////////////////////////////////////////////
$( document ).ready( function() {
    $(function () {
    // $('.abcdefgh').hide();
        $('#id_checking-0-rspect_right_human').change(function () {
          var coppy_right=$("#id_checking-0-rspect_right_human").val()
          switch(coppy_right) {
            case '0':
                $("#id_checking-0-mark_rspect_right_human").val('1');
              break;
            case '1':
                $("#id_checking-0-mark_rspect_right_human").val('0');
              break;             
            default:
                $("#id_checking-0-mark_rspect_right_human").val('0');
                
          }    
    
        });        
    });
    });

//all for notes and export values from parent model 
$(document).ready(function(){
    //for fill field
    //$('##id_first_name').removeAttr('readonly');
    $("#id_checking-0-tiitle_of_state").val($('#id_first_name').val()+' '+ $('#id_last_name').val()+' ' +'من'+'  '+$('#id_city').val());
    //$('#id_first_name').add('readonly');
    //family number into family state
    $("#id_checking-0-family_state_1").val($('#id_number_kids').val());
    $("#id_checking-0-first_recmond_name").val($('#id_recmond_1').val());
    $("#id_checking-0-second_recmond_name").val($('#id_recmond_2').val());
    


    //here is you can write placeholder for all fields that exist in inline form
   // $("#id_checking-0-cruntly_adre").attr('placeholder', 'hello' )
    //$("#id_checking-0-confirm_stat").val($('#id_type_of_dmande').value());
    //This is a simple way of getting the DAYS between two dates** 
    
    $("#id_checking-0-number_of_year_exprince").val( $("#id_start_date").val())

    var demand=$("#id_type_of_dmande").val()
    var edu_point=$("#id_educatton_level").val()
    var media_memeber=$("#id_org_memeber").val()
    var medical_state=$("#id_medical_state_inf").val()
    var paid1_job=$("#id_paid_job").val()

    var a=parseInt($("#id_checking-0-member_in_journal").val())
    var b=parseInt($("#id_checking-0-educatton_level_1").val())
    var c=parseInt($("#id_checking-0-medical_state").val())
    var d=parseInt($("#id_checking-0-note_paid_job").val())
    var f=parseInt($("#id_checking-0-mark_rspect_right_human").val())
    var t=parseInt($("#id_checking-0-mark_rspect_coppyright").val())
    var g=parseInt($("#id_checking-0-rspect_legal_coppyright").val())
    var h=parseInt($("#id_checking-0-note_of_year_experince").val())

    $("#id_checking-0-total_of_note").val(a+b+c+d+h+f+t)

    //give the type of the demande note
    switch(demand) {
        case '0':
            $("#id_checking-0-confirm_stat").val('دعم معيش');
          break;
        case '1':
            $("#id_checking-0-confirm_stat").val('إيجاد فرصة عمل');
          break;
          case '2':
            $("#id_checking-0-confirm_stat").val('خروج آمن');
          break;
          case '3':
            $("#id_checking-0-confirm_stat").val('خروج دعم ملف اللجوء - تأشيرات خروج');
          break;
          case '4':
            $("#id_checking-0-confirm_stat").val('دعم تقني وبطاقات صحفية');
          break;
          case '5':
            $("#id_checking-0-confirm_stat").val('دعم طبي');
          break;
          case '6':
            $("#id_checking-0-confirm_stat").val('غير ذلك');
          break;
        default:
            $("#id_checking-0-confirm_stat").val('0');
            
      } 
      //give the eduction level note
      switch(edu_point) {
        case '0':
            $("#id_checking-0-educatton_level_1").val('1');
          break;
        case '1':
            $("#id_checking-0-educatton_level_1").val('2');
          break;
          case '2':
            $("#id_checking-0-educatton_level_1").val('0');
          break;
        default:
            $("#id_checking-0-educatton_level_1").val('0');
            
      } 
     //give note for the member ship in media commity
      switch(media_memeber) {
        case '0':
            $("#id_checking-0-member_in_journal").val('1');
          break;
        case '1':
            $("#id_checking-0-member_in_journal").val('0');
          break;
          
        default:
            $("#id_checking-0-member_in_journal").val('0');
            
      } 
      switch(medical_state) {
        case '0':
            $("#id_checking-0-medical_state").val('1');
          break;
        case '1':
            $("#id_checking-0-medical_state").val('0');
          break;
          
        default:
            $("#id_checking-0-medical_state").val('0');
            
      } 
      switch(paid1_job) {
        case '0':
            $("#id_checking-0-note_paid_job").val('1');
          break;
        case '1':
            $("#id_checking-0-note_paid_job").val('0');
          break;
          
        default:
            $("#id_checking-0-note_paid_job").val('0');
            
      } 
     

    

    //$("#id_item-0-test3").val(a+b)
    //if (b>2) {
       // $("#id_state_step").attr("disabled",true);;
   // }
   });(django.jQuery);
