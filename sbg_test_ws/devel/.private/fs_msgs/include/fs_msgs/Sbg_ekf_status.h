// Generated by gencpp from file fs_msgs/Sbg_ekf_status.msg
// DO NOT EDIT!


#ifndef FS_MSGS_MESSAGE_SBG_EKF_STATUS_H
#define FS_MSGS_MESSAGE_SBG_EKF_STATUS_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace fs_msgs
{
template <class ContainerAllocator>
struct Sbg_ekf_status_
{
  typedef Sbg_ekf_status_<ContainerAllocator> Type;

  Sbg_ekf_status_()
    : COMPUTATION_MODE(0)
    , ATTITUDE_VALID(false)
    , HEADING_VALID(false)
    , VELOCITY_VALID(false)
    , POSITION_VALID(false)
    , VERT_REF_USED(false)
    , MAG_REF_USED(false)
    , GPS1_VEL_USED(false)
    , GPS1_POS_USED(false)
    , GPS1_HDT_USED(false)
    , GPS2_VEL_USED(false)
    , GPS2_POS_USED(false)
    , GPS2_HDT_USED(false)
    , ODO_USED(false)
    , DVL_BT_USED(false)
    , DVL_WT_USED(false)
    , USBL_USED(false)
    , AIR_DATA_USED(false)
    , ZUPT_USED(false)
    , ALIGN_VALID(false)
    , DEPTH_USED(false)  {
    }
  Sbg_ekf_status_(const ContainerAllocator& _alloc)
    : COMPUTATION_MODE(0)
    , ATTITUDE_VALID(false)
    , HEADING_VALID(false)
    , VELOCITY_VALID(false)
    , POSITION_VALID(false)
    , VERT_REF_USED(false)
    , MAG_REF_USED(false)
    , GPS1_VEL_USED(false)
    , GPS1_POS_USED(false)
    , GPS1_HDT_USED(false)
    , GPS2_VEL_USED(false)
    , GPS2_POS_USED(false)
    , GPS2_HDT_USED(false)
    , ODO_USED(false)
    , DVL_BT_USED(false)
    , DVL_WT_USED(false)
    , USBL_USED(false)
    , AIR_DATA_USED(false)
    , ZUPT_USED(false)
    , ALIGN_VALID(false)
    , DEPTH_USED(false)  {
  (void)_alloc;
    }



   typedef uint8_t _COMPUTATION_MODE_type;
  _COMPUTATION_MODE_type COMPUTATION_MODE;

   typedef uint8_t _ATTITUDE_VALID_type;
  _ATTITUDE_VALID_type ATTITUDE_VALID;

   typedef uint8_t _HEADING_VALID_type;
  _HEADING_VALID_type HEADING_VALID;

   typedef uint8_t _VELOCITY_VALID_type;
  _VELOCITY_VALID_type VELOCITY_VALID;

   typedef uint8_t _POSITION_VALID_type;
  _POSITION_VALID_type POSITION_VALID;

   typedef uint8_t _VERT_REF_USED_type;
  _VERT_REF_USED_type VERT_REF_USED;

   typedef uint8_t _MAG_REF_USED_type;
  _MAG_REF_USED_type MAG_REF_USED;

   typedef uint8_t _GPS1_VEL_USED_type;
  _GPS1_VEL_USED_type GPS1_VEL_USED;

   typedef uint8_t _GPS1_POS_USED_type;
  _GPS1_POS_USED_type GPS1_POS_USED;

   typedef uint8_t _GPS1_HDT_USED_type;
  _GPS1_HDT_USED_type GPS1_HDT_USED;

   typedef uint8_t _GPS2_VEL_USED_type;
  _GPS2_VEL_USED_type GPS2_VEL_USED;

   typedef uint8_t _GPS2_POS_USED_type;
  _GPS2_POS_USED_type GPS2_POS_USED;

   typedef uint8_t _GPS2_HDT_USED_type;
  _GPS2_HDT_USED_type GPS2_HDT_USED;

   typedef uint8_t _ODO_USED_type;
  _ODO_USED_type ODO_USED;

   typedef uint8_t _DVL_BT_USED_type;
  _DVL_BT_USED_type DVL_BT_USED;

   typedef uint8_t _DVL_WT_USED_type;
  _DVL_WT_USED_type DVL_WT_USED;

   typedef uint8_t _USBL_USED_type;
  _USBL_USED_type USBL_USED;

   typedef uint8_t _AIR_DATA_USED_type;
  _AIR_DATA_USED_type AIR_DATA_USED;

   typedef uint8_t _ZUPT_USED_type;
  _ZUPT_USED_type ZUPT_USED;

   typedef uint8_t _ALIGN_VALID_type;
  _ALIGN_VALID_type ALIGN_VALID;

   typedef uint8_t _DEPTH_USED_type;
  _DEPTH_USED_type DEPTH_USED;





  typedef boost::shared_ptr< ::fs_msgs::Sbg_ekf_status_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::fs_msgs::Sbg_ekf_status_<ContainerAllocator> const> ConstPtr;

}; // struct Sbg_ekf_status_

typedef ::fs_msgs::Sbg_ekf_status_<std::allocator<void> > Sbg_ekf_status;

typedef boost::shared_ptr< ::fs_msgs::Sbg_ekf_status > Sbg_ekf_statusPtr;
typedef boost::shared_ptr< ::fs_msgs::Sbg_ekf_status const> Sbg_ekf_statusConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::fs_msgs::Sbg_ekf_status_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::fs_msgs::Sbg_ekf_status_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace fs_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'fs_msgs': ['/home/joar/KTHFS/sbg_test_ws/src/fs_msgs/msg'], 'actionlib_msgs': ['/opt/ros/melodic/share/actionlib_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/melodic/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::fs_msgs::Sbg_ekf_status_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::fs_msgs::Sbg_ekf_status_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::fs_msgs::Sbg_ekf_status_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::fs_msgs::Sbg_ekf_status_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::fs_msgs::Sbg_ekf_status_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::fs_msgs::Sbg_ekf_status_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::fs_msgs::Sbg_ekf_status_<ContainerAllocator> >
{
  static const char* value()
  {
    return "464794a3821aebe67baf95cbfb19fb69";
  }

  static const char* value(const ::fs_msgs::Sbg_ekf_status_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x464794a3821aebe6ULL;
  static const uint64_t static_value2 = 0x7baf95cbfb19fb69ULL;
};

template<class ContainerAllocator>
struct DataType< ::fs_msgs::Sbg_ekf_status_<ContainerAllocator> >
{
  static const char* value()
  {
    return "fs_msgs/Sbg_ekf_status";
  }

  static const char* value(const ::fs_msgs::Sbg_ekf_status_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::fs_msgs::Sbg_ekf_status_<ContainerAllocator> >
{
  static const char* value()
  {
    return "uint8 COMPUTATION_MODE\n"
"bool ATTITUDE_VALID\n"
"bool HEADING_VALID\n"
"bool VELOCITY_VALID\n"
"bool POSITION_VALID\n"
"bool VERT_REF_USED\n"
"bool MAG_REF_USED\n"
"bool GPS1_VEL_USED\n"
"bool GPS1_POS_USED\n"
"bool GPS1_HDT_USED\n"
"bool GPS2_VEL_USED\n"
"bool GPS2_POS_USED\n"
"bool GPS2_HDT_USED\n"
"bool ODO_USED\n"
"bool DVL_BT_USED\n"
"bool DVL_WT_USED\n"
"bool USBL_USED\n"
"bool AIR_DATA_USED\n"
"bool ZUPT_USED\n"
"bool ALIGN_VALID\n"
"bool DEPTH_USED\n"
"\n"
;
  }

  static const char* value(const ::fs_msgs::Sbg_ekf_status_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::fs_msgs::Sbg_ekf_status_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.COMPUTATION_MODE);
      stream.next(m.ATTITUDE_VALID);
      stream.next(m.HEADING_VALID);
      stream.next(m.VELOCITY_VALID);
      stream.next(m.POSITION_VALID);
      stream.next(m.VERT_REF_USED);
      stream.next(m.MAG_REF_USED);
      stream.next(m.GPS1_VEL_USED);
      stream.next(m.GPS1_POS_USED);
      stream.next(m.GPS1_HDT_USED);
      stream.next(m.GPS2_VEL_USED);
      stream.next(m.GPS2_POS_USED);
      stream.next(m.GPS2_HDT_USED);
      stream.next(m.ODO_USED);
      stream.next(m.DVL_BT_USED);
      stream.next(m.DVL_WT_USED);
      stream.next(m.USBL_USED);
      stream.next(m.AIR_DATA_USED);
      stream.next(m.ZUPT_USED);
      stream.next(m.ALIGN_VALID);
      stream.next(m.DEPTH_USED);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct Sbg_ekf_status_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::fs_msgs::Sbg_ekf_status_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::fs_msgs::Sbg_ekf_status_<ContainerAllocator>& v)
  {
    s << indent << "COMPUTATION_MODE: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.COMPUTATION_MODE);
    s << indent << "ATTITUDE_VALID: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.ATTITUDE_VALID);
    s << indent << "HEADING_VALID: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.HEADING_VALID);
    s << indent << "VELOCITY_VALID: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.VELOCITY_VALID);
    s << indent << "POSITION_VALID: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.POSITION_VALID);
    s << indent << "VERT_REF_USED: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.VERT_REF_USED);
    s << indent << "MAG_REF_USED: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.MAG_REF_USED);
    s << indent << "GPS1_VEL_USED: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.GPS1_VEL_USED);
    s << indent << "GPS1_POS_USED: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.GPS1_POS_USED);
    s << indent << "GPS1_HDT_USED: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.GPS1_HDT_USED);
    s << indent << "GPS2_VEL_USED: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.GPS2_VEL_USED);
    s << indent << "GPS2_POS_USED: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.GPS2_POS_USED);
    s << indent << "GPS2_HDT_USED: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.GPS2_HDT_USED);
    s << indent << "ODO_USED: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.ODO_USED);
    s << indent << "DVL_BT_USED: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.DVL_BT_USED);
    s << indent << "DVL_WT_USED: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.DVL_WT_USED);
    s << indent << "USBL_USED: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.USBL_USED);
    s << indent << "AIR_DATA_USED: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.AIR_DATA_USED);
    s << indent << "ZUPT_USED: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.ZUPT_USED);
    s << indent << "ALIGN_VALID: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.ALIGN_VALID);
    s << indent << "DEPTH_USED: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.DEPTH_USED);
  }
};

} // namespace message_operations
} // namespace ros

#endif // FS_MSGS_MESSAGE_SBG_EKF_STATUS_H
