"""
Test suite for the oneforall.components module.

This module contains comprehensive tests for all component classes including:
- Component (base class)
- Text
- Button
- Container

Test coverage includes:
- Initialization and attribute setting
- Rendering functionality
- Child component management
- HTML escaping and security
- CSS class merging
"""

import html
from unittest.mock import Mock, patch

import pytest

from oneforall.components import Button, Component, Container, Text


class TestComponent:
    """Test cases for the base Component class."""

    def test_component_initialization_default(self):
        """Test Component initialization with default parameters."""
        component = Component()

        assert component.id.startswith("c_")
        assert len(component.id) == 10  # "c_" + 8 hex characters
        assert component.className == []
        assert component.attrs == {}
        assert component.children == []

    def test_component_initialization_with_params(self):
        """Test Component initialization with custom parameters."""
        class_name = ["test-class", "another-class"]
        attrs = {"data-test": "value", "role": "button"}

        component = Component(className=class_name, attrs=attrs)

        assert component.className == class_name
        assert component.attrs == attrs
        assert component.children == []

    def test_component_add_child(self):
        """Test adding child components."""
        parent = Component()
        child1 = Component()
        child2 = Component()

        returned_child1 = parent.add(child1)
        returned_child2 = parent.add(child2)

        assert len(parent.children) == 2
        assert parent.children[0] == child1
        assert parent.children[1] == child2
        assert returned_child1 == child1
        assert returned_child2 == child2

    def test_component_render_not_implemented(self):
        """Test that base Component render method raises NotImplementedError."""
        component = Component()

        with pytest.raises(NotImplementedError):
            component.render()

    def test_component_unique_ids(self):
        """Test that each component gets a unique ID."""
        components = [Component() for _ in range(10)]
        ids = [comp.id for comp in components]

        assert len(set(ids)) == len(ids)  # All IDs should be unique


class TestText:
    """Test cases for the Text component."""

    def test_text_initialization_basic(self):
        """Test Text component initialization with basic parameters."""
        text_value = "Hello, World!"
        text_comp = Text(text_value)

        assert text_comp.text == text_value
        assert text_comp._value == text_value
        assert text_comp.default_class == ""
        assert text_comp._window is None

    def test_text_initialization_with_classes(self):
        """Test Text component initialization with CSS classes."""
        text_value = "Test text"
        class_name = "text-lg font-bold"
        default_class = "text-gray-800"

        text_comp = Text(text_value, className=class_name, default_class=default_class)

        assert text_comp.text == text_value
        assert text_comp.className == class_name
        assert text_comp.default_class == default_class

    def test_text_property_getter_setter(self):
        """Test text property getter and setter."""
        initial_text = "Initial text"
        new_text = "Updated text"
        text_comp = Text(initial_text)

        # Test getter
        assert text_comp.text == initial_text

        # Test setter without window
        text_comp.text = new_text
        assert text_comp.text == new_text
        assert text_comp._value == new_text

    def test_text_property_setter_with_window(self):
        """Test text property setter with window refresh."""
        text_comp = Text("Initial text")
        mock_window = Mock()
        text_comp._window = mock_window

        text_comp.text = "New text"

        assert text_comp.text == "New text"
        mock_window.refresh.assert_called_once()

    @patch("oneforall.components.merge_classes")
    def test_text_render(self, mock_merge_classes):
        """Test Text component rendering."""
        mock_merge_classes.return_value = "merged-classes"

        text_value = "Test <script>alert('xss')</script> content"
        text_comp = Text(
            text_value, className="custom-class", default_class="default-class"
        )

        result = text_comp.render()

        # Check that merge_classes was called with correct arguments
        mock_merge_classes.assert_called_once_with("default-class", "custom-class")

        # Check HTML structure
        expected_escaped_text = html.escape(text_value)
        assert f"id='{text_comp.id}'" in result
        assert "class='merged-classes'" in result
        assert expected_escaped_text in result
        assert "<div" in result and "</div>" in result

        # Ensure XSS content is escaped
        assert "<script>" not in result
        assert "&lt;script&gt;" in result

    def test_text_html_escaping(self):
        """Test that HTML content is properly escaped."""
        dangerous_text = '<img src="x" onerror="alert(1)">'
        text_comp = Text(dangerous_text)

        result = text_comp.render()

        # Ensure dangerous HTML is escaped
        assert "<img" not in result
        assert "&lt;img" in result
        assert "onerror" not in result or "&quot;" in result


class TestButton:
    """Test cases for the Button component."""

    def test_button_initialization_basic(self):
        """Test Button component initialization with basic parameters."""
        label = "Click me"
        button = Button(label)

        assert button.label == label
        assert button.on_click is None
        assert button.default_class == ""

    def test_button_initialization_with_callback(self):
        """Test Button component initialization with click callback."""
        label = "Submit"
        callback = Mock()
        class_name = "btn-primary"
        default_class = "btn"

        button = Button(
            label, on_click=callback, className=class_name, default_class=default_class
        )

        assert button.label == label
        assert button.on_click == callback
        assert button.className == class_name
        assert button.default_class == default_class

    @patch("oneforall.components.merge_classes")
    def test_button_render(self, mock_merge_classes):
        """Test Button component rendering."""
        mock_merge_classes.return_value = "merged-button-classes"

        label = "Test <b>Button</b>"
        callback = Mock()
        button = Button(
            label, on_click=callback, className="custom", default_class="default"
        )

        result = button.render()

        # Check that merge_classes was called
        mock_merge_classes.assert_called_once_with("default", "custom")

        # Check HTML structure
        expected_escaped_label = html.escape(label)
        assert f"id='{button.id}'" in result
        assert "class='merged-button-classes'" in result
        assert expected_escaped_label in result
        assert f"onclick=\"window.pywebview.api.call('{button.id}', {{}})\"" in result
        assert "<button" in result and "</button>" in result

        # Ensure HTML in label is escaped
        assert "<b>" not in result
        assert "&lt;b&gt;" in result

    def test_button_render_without_callback(self):
        """Test Button rendering without click callback."""
        button = Button("No callback")

        result = button.render()

        # Should still have onclick attribute even without callback
        assert f"onclick=\"window.pywebview.api.call('{button.id}', {{}})\"" in result


class TestContainer:
    """Test cases for the Container component."""

    def test_container_initialization(self):
        """Test Container component initialization."""
        container = Container()

        assert container.children == []
        assert container.default_class == ""

    def test_container_initialization_with_classes(self):
        """Test Container initialization with CSS classes."""
        class_name = "flex flex-col"
        default_class = "container"

        container = Container(className=class_name, default_class=default_class)

        assert container.className == class_name
        assert container.default_class == default_class

    def test_container_add_child(self):
        """Test adding children to container."""
        container = Container()
        child1 = Text("Child 1")
        child2 = Button("Child 2")

        container.add(child1)
        container.add(child2)

        assert len(container.children) == 2
        assert container.children[0] == child1
        assert container.children[1] == child2

    @patch("oneforall.components.merge_classes")
    def test_container_render_empty(self, mock_merge_classes):
        """Test Container rendering with no children."""
        mock_merge_classes.return_value = "merged-container-classes"

        container = Container(className="custom", default_class="default")

        result = container.render()

        mock_merge_classes.assert_called_once_with("default", "custom")

        assert f"id='{container.id}'" in result
        assert "class='merged-container-classes'" in result
        assert "<div" in result and "</div>" in result
        # Should have empty content between div tags
        assert (
            f"<div id='{container.id}' class='merged-container-classes'></div>"
            == result
        )

    @patch("oneforall.components.merge_classes")
    def test_container_render_with_children(self, mock_merge_classes):
        """Test Container rendering with children."""
        mock_merge_classes.return_value = "container-classes"

        container = Container()

        # Create mock children with render methods
        child1 = Mock()
        child1.render.return_value = "<div>Child 1</div>"
        child2 = Mock()
        child2.render.return_value = "<span>Child 2</span>"

        container.add(child1)
        container.add(child2)

        result = container.render()

        # Check that children's render methods were called
        child1.render.assert_called_once()
        child2.render.assert_called_once()

        # Check that children's HTML is included
        assert "<div>Child 1</div>" in result
        assert "<span>Child 2</span>" in result
        assert f"id='{container.id}'" in result
        assert "class='container-classes'" in result

    def test_container_nested_structure(self):
        """Test nested container structure."""
        parent_container = Container()
        child_container = Container()
        text_component = Text("Nested text")

        child_container.add(text_component)
        parent_container.add(child_container)

        assert len(parent_container.children) == 1
        assert parent_container.children[0] == child_container
        assert len(child_container.children) == 1
        assert child_container.children[0] == text_component


class TestIntegration:
    """Integration tests for component interactions."""

    def test_complex_component_tree(self):
        """Test rendering a complex component tree."""
        # Create a complex structure
        root = Container(className="app")
        header = Container(className="header")
        title = Text("My App", className="title")
        nav_button = Button("Menu", className="nav-btn")

        content = Container(className="content")
        paragraph = Text("Welcome to my application!")
        action_button = Button("Get Started", className="cta-btn")

        # Build the tree
        header.add(title)
        header.add(nav_button)
        content.add(paragraph)
        content.add(action_button)
        root.add(header)
        root.add(content)

        # Render and verify structure
        result = root.render()

        # Should contain all components
        assert "My App" in result
        assert "Menu" in result
        assert "Welcome to my application!" in result
        assert "Get Started" in result

        # Should have proper nesting structure
        assert result.count("<div") >= 3  # root, header, content containers
        assert result.count("<button") == 2  # nav and action buttons

    @patch("oneforall.components.merge_classes")
    def test_css_class_merging_called_correctly(self, mock_merge_classes):
        """Test that CSS class merging is called correctly for all components."""
        mock_merge_classes.return_value = "merged"

        # Test all component types
        text = Text("test", className="text-class", default_class="text-default")
        button = Button("test", className="btn-class", default_class="btn-default")
        container = Container(
            className="container-class", default_class="container-default"
        )

        text.render()
        button.render()
        container.render()

        # Verify merge_classes was called for each component
        expected_calls = [
            ("text-default", "text-class"),
            ("btn-default", "btn-class"),
            ("container-default", "container-class"),
        ]

        actual_calls = [call.args for call in mock_merge_classes.call_args_list]
        assert actual_calls == expected_calls


# Fixtures for common test data
@pytest.fixture
def sample_text():
    """Fixture providing a sample Text component."""
    return Text("Sample text", className="test-class")


@pytest.fixture
def sample_button():
    """Fixture providing a sample Button component."""
    return Button("Sample button", className="test-btn")


@pytest.fixture
def sample_container():
    """Fixture providing a sample Container component."""
    return Container(className="test-container")


@pytest.fixture
def mock_callback():
    """Fixture providing a mock callback function."""
    return Mock()


# Parametrized tests for edge cases
@pytest.mark.parametrize(
    "text_input,expected_escaped",
    [
        ("Normal text", "Normal text"),
        (
            "<script>alert('xss')</script>",
            "&lt;script&gt;alert(&#x27;xss&#x27;)&lt;/script&gt;",
        ),
        ("Text with & ampersand", "Text with &amp; ampersand"),
        (
            "Quotes: \"double\" and 'single'",
            "Quotes: &quot;double&quot; and &#x27;single&#x27;",
        ),
        ("", ""),  # Empty string
        ("Unicode: 🚀 emoji", "Unicode: 🚀 emoji"),
    ],
)
def test_text_html_escaping_parametrized(text_input, expected_escaped):
    """Parametrized test for HTML escaping in Text component."""
    text_comp = Text(text_input)
    result = text_comp.render()
    assert expected_escaped in result


@pytest.mark.parametrize(
    "label_input,expected_escaped",
    [
        ("Normal button", "Normal button"),
        ("<b>Bold</b> button", "&lt;b&gt;Bold&lt;/b&gt; button"),
        ("Button with & symbol", "Button with &amp; symbol"),
        ("", ""),  # Empty label
    ],
)
def test_button_label_escaping_parametrized(label_input, expected_escaped):
    """Parametrized test for HTML escaping in Button labels."""
    button = Button(label_input)
    result = button.render()
    assert expected_escaped in result
