// Generated by gencpp from file fs_msgs/Cone.msg
// DO NOT EDIT!


#ifndef FS_MSGS_MESSAGE_CONE_H
#define FS_MSGS_MESSAGE_CONE_H


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
struct Cone_
{
  typedef Cone_<ContainerAllocator> Type;

  Cone_()
    : x(0.0)
    , y(0.0)
    , color(0)
    , covariance()
    , probability(0.0)  {
      covariance.assign(0.0);
  }
  Cone_(const ContainerAllocator& _alloc)
    : x(0.0)
    , y(0.0)
    , color(0)
    , covariance()
    , probability(0.0)  {
  (void)_alloc;
      covariance.assign(0.0);
  }



   typedef double _x_type;
  _x_type x;

   typedef double _y_type;
  _y_type y;

   typedef uint8_t _color_type;
  _color_type color;

   typedef boost::array<double, 4>  _covariance_type;
  _covariance_type covariance;

   typedef double _probability_type;
  _probability_type probability;



  enum {
    UNDEFINED = 0u,
    YELLOW = 1u,
    BLUE = 2u,
    SMALL_ORANGE = 3u,
    BIG_ORANGE = 4u,
  };


  typedef boost::shared_ptr< ::fs_msgs::Cone_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::fs_msgs::Cone_<ContainerAllocator> const> ConstPtr;

}; // struct Cone_

typedef ::fs_msgs::Cone_<std::allocator<void> > Cone;

typedef boost::shared_ptr< ::fs_msgs::Cone > ConePtr;
typedef boost::shared_ptr< ::fs_msgs::Cone const> ConeConstPtr;

// constants requiring out of line definition

   

   

   

   

   



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::fs_msgs::Cone_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::fs_msgs::Cone_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace fs_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'fs_msgs': ['/home/jack/KTHFS/sbg_test_ws/src/fs_msgs/msg'], 'actionlib_msgs': ['/opt/ros/melodic/share/actionlib_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/melodic/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::fs_msgs::Cone_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::fs_msgs::Cone_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::fs_msgs::Cone_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::fs_msgs::Cone_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::fs_msgs::Cone_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::fs_msgs::Cone_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::fs_msgs::Cone_<ContainerAllocator> >
{
  static const char* value()
  {
    return "7c4e8c6cb0ce4d9bafe06a39d73f0f9e";
  }

  static const char* value(const ::fs_msgs::Cone_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x7c4e8c6cb0ce4d9bULL;
  static const uint64_t static_value2 = 0xafe06a39d73f0f9eULL;
};

template<class ContainerAllocator>
struct DataType< ::fs_msgs::Cone_<ContainerAllocator> >
{
  static const char* value()
  {
    return "fs_msgs/Cone";
  }

  static const char* value(const ::fs_msgs::Cone_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::fs_msgs::Cone_<ContainerAllocator> >
{
  static const char* value()
  {
    return "#\n"
"# Description of a cone\n"
"#\n"
"\n"
"# 2D-position of the cone\n"
"float64 x\n"
"float64 y\n"
"\n"
"# Color of the cone\n"
"uint8 UNDEFINED = 0\n"
"uint8 YELLOW = 1\n"
"uint8 BLUE = 2\n"
"uint8 SMALL_ORANGE = 3\n"
"uint8 BIG_ORANGE = 4\n"
"\n"
"uint8 color\n"
"\n"
"# Covariance on the position [m^2] (2x2 matrix in row-major order)\n"
"float64[4] covariance\n"
"\n"
"# Confidence in the detection\n"
"float64 probability\n"
;
  }

  static const char* value(const ::fs_msgs::Cone_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::fs_msgs::Cone_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.x);
      stream.next(m.y);
      stream.next(m.color);
      stream.next(m.covariance);
      stream.next(m.probability);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct Cone_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::fs_msgs::Cone_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::fs_msgs::Cone_<ContainerAllocator>& v)
  {
    s << indent << "x: ";
    Printer<double>::stream(s, indent + "  ", v.x);
    s << indent << "y: ";
    Printer<double>::stream(s, indent + "  ", v.y);
    s << indent << "color: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.color);
    s << indent << "covariance[]" << std::endl;
    for (size_t i = 0; i < v.covariance.size(); ++i)
    {
      s << indent << "  covariance[" << i << "]: ";
      Printer<double>::stream(s, indent + "  ", v.covariance[i]);
    }
    s << indent << "probability: ";
    Printer<double>::stream(s, indent + "  ", v.probability);
  }
};

} // namespace message_operations
} // namespace ros

#endif // FS_MSGS_MESSAGE_CONE_H
