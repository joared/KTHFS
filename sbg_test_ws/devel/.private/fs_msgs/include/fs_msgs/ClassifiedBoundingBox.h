// Generated by gencpp from file fs_msgs/ClassifiedBoundingBox.msg
// DO NOT EDIT!


#ifndef FS_MSGS_MESSAGE_CLASSIFIEDBOUNDINGBOX_H
#define FS_MSGS_MESSAGE_CLASSIFIEDBOUNDINGBOX_H


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
struct ClassifiedBoundingBox_
{
  typedef ClassifiedBoundingBox_<ContainerAllocator> Type;

  ClassifiedBoundingBox_()
    : Class()
    , probability(0.0)
    , xmin(0)
    , ymin(0)
    , xmax(0)
    , ymax(0)  {
    }
  ClassifiedBoundingBox_(const ContainerAllocator& _alloc)
    : Class(_alloc)
    , probability(0.0)
    , xmin(0)
    , ymin(0)
    , xmax(0)
    , ymax(0)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _Class_type;
  _Class_type Class;

   typedef double _probability_type;
  _probability_type probability;

   typedef int64_t _xmin_type;
  _xmin_type xmin;

   typedef int64_t _ymin_type;
  _ymin_type ymin;

   typedef int64_t _xmax_type;
  _xmax_type xmax;

   typedef int64_t _ymax_type;
  _ymax_type ymax;





  typedef boost::shared_ptr< ::fs_msgs::ClassifiedBoundingBox_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::fs_msgs::ClassifiedBoundingBox_<ContainerAllocator> const> ConstPtr;

}; // struct ClassifiedBoundingBox_

typedef ::fs_msgs::ClassifiedBoundingBox_<std::allocator<void> > ClassifiedBoundingBox;

typedef boost::shared_ptr< ::fs_msgs::ClassifiedBoundingBox > ClassifiedBoundingBoxPtr;
typedef boost::shared_ptr< ::fs_msgs::ClassifiedBoundingBox const> ClassifiedBoundingBoxConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::fs_msgs::ClassifiedBoundingBox_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::fs_msgs::ClassifiedBoundingBox_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace fs_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'fs_msgs': ['/home/joar/KTHFS/sbg_test_ws/src/fs_msgs/msg'], 'actionlib_msgs': ['/opt/ros/melodic/share/actionlib_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/melodic/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::fs_msgs::ClassifiedBoundingBox_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::fs_msgs::ClassifiedBoundingBox_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::fs_msgs::ClassifiedBoundingBox_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::fs_msgs::ClassifiedBoundingBox_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::fs_msgs::ClassifiedBoundingBox_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::fs_msgs::ClassifiedBoundingBox_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::fs_msgs::ClassifiedBoundingBox_<ContainerAllocator> >
{
  static const char* value()
  {
    return "8434cf5c7ed632005efa1b05bb45ca2a";
  }

  static const char* value(const ::fs_msgs::ClassifiedBoundingBox_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x8434cf5c7ed63200ULL;
  static const uint64_t static_value2 = 0x5efa1b05bb45ca2aULL;
};

template<class ContainerAllocator>
struct DataType< ::fs_msgs::ClassifiedBoundingBox_<ContainerAllocator> >
{
  static const char* value()
  {
    return "fs_msgs/ClassifiedBoundingBox";
  }

  static const char* value(const ::fs_msgs::ClassifiedBoundingBox_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::fs_msgs::ClassifiedBoundingBox_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string Class\n"
"float64 probability\n"
"int64 xmin\n"
"int64 ymin\n"
"int64 xmax\n"
"int64 ymax\n"
;
  }

  static const char* value(const ::fs_msgs::ClassifiedBoundingBox_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::fs_msgs::ClassifiedBoundingBox_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.Class);
      stream.next(m.probability);
      stream.next(m.xmin);
      stream.next(m.ymin);
      stream.next(m.xmax);
      stream.next(m.ymax);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct ClassifiedBoundingBox_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::fs_msgs::ClassifiedBoundingBox_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::fs_msgs::ClassifiedBoundingBox_<ContainerAllocator>& v)
  {
    s << indent << "Class: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.Class);
    s << indent << "probability: ";
    Printer<double>::stream(s, indent + "  ", v.probability);
    s << indent << "xmin: ";
    Printer<int64_t>::stream(s, indent + "  ", v.xmin);
    s << indent << "ymin: ";
    Printer<int64_t>::stream(s, indent + "  ", v.ymin);
    s << indent << "xmax: ";
    Printer<int64_t>::stream(s, indent + "  ", v.xmax);
    s << indent << "ymax: ";
    Printer<int64_t>::stream(s, indent + "  ", v.ymax);
  }
};

} // namespace message_operations
} // namespace ros

#endif // FS_MSGS_MESSAGE_CLASSIFIEDBOUNDINGBOX_H
